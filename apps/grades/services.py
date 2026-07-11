from decimal import Decimal, InvalidOperation

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction
from django.utils import timezone

from apps.accounts.models import User
from apps.audit.models import AuditEvent
from apps.schools.models import ReportPeriod
from apps.subjects.models import TeachingAssignment

from .models import Grade, GradeSheet


class GradeConflictError(Exception):
    pass


def can_manage_assignment(user, assignment):
    return (
        user.is_superuser
        or user.role in {User.Role.ADMIN, User.Role.SCHOOL_MANAGEMENT}
        or assignment.teacher_id == user.id
    )


def can_view_class(user, school_class):
    return (
        user.is_superuser
        or user.role in {User.Role.ADMIN, User.Role.SCHOOL_MANAGEMENT}
        or school_class.class_teacher_id == user.id
        or school_class.teaching_assignments.filter(teacher=user).exists()
    )


@transaction.atomic
def save_grade_values(*, assignment, user, values, versions):
    assignment = TeachingAssignment.objects.select_related("subject", "report_period", "school_class").get(
        pk=assignment.pk
    )
    if not can_manage_assignment(user, assignment):
        raise PermissionDenied
    if assignment.report_period.status != ReportPeriod.Status.OPEN:
        raise ValidationError("Die Zeugnisperiode ist nicht für Eingaben geöffnet.")
    sheet, _ = GradeSheet.objects.select_for_update().get_or_create(assignment=assignment)
    if sheet.status == GradeSheet.Status.COMPLETED:
        raise ValidationError("Die Noteneingabe ist abgeschlossen und gesperrt.")

    student_ids = set(assignment.school_class.enrollments.values_list("student_id", flat=True))
    for student_id, raw_value in values.items():
        if student_id not in student_ids:
            raise PermissionDenied
        try:
            value = Decimal(raw_value.replace(",", "."))
        except (InvalidOperation, AttributeError) as exc:
            raise ValidationError("Bitte eine gültige Note eingeben.") from exc
        grade = Grade.objects.select_for_update().filter(sheet=sheet, student_id=student_id).first()
        expected_version = versions.get(student_id, 0)
        if grade and grade.version != expected_version:
            raise GradeConflictError("Die Note wurde zwischenzeitlich geändert. Bitte laden Sie die Seite neu.")
        old_values = {} if grade is None else {"value": str(grade.value), "version": grade.version}
        if grade is None:
            grade = Grade(sheet=sheet, student_id=student_id, value=value, changed_by=user)
        else:
            grade.value = value
            grade.version += 1
            grade.changed_by = user
        grade.full_clean()
        grade.save()
        AuditEvent.objects.create(
            actor=user,
            action="grade_saved",
            object_type="Grade",
            object_id=str(grade.pk),
            old_values=old_values,
            new_values={"value": str(grade.value), "version": grade.version},
        )
    return sheet


@transaction.atomic
def complete_sheet(*, assignment, user):
    if not can_manage_assignment(user, assignment):
        raise PermissionDenied
    sheet, _ = GradeSheet.objects.select_for_update().get_or_create(assignment=assignment)
    expected = assignment.school_class.enrollments.count()
    if not expected or sheet.grades.count() != expected:
        raise ValidationError("Für den Abschluss müssen alle Schüler eine Note besitzen.")
    sheet.status = GradeSheet.Status.COMPLETED
    sheet.completed_by = user
    sheet.completed_at = timezone.now()
    sheet.save()
    AuditEvent.objects.create(
        actor=user, action="grade_sheet_completed", object_type="GradeSheet", object_id=str(sheet.pk)
    )
    return sheet


@transaction.atomic
def reopen_sheet(*, sheet, user):
    if not (user.is_superuser or user.role == User.Role.ADMIN):
        raise PermissionDenied
    sheet = GradeSheet.objects.select_for_update().get(pk=sheet.pk)
    sheet.status = GradeSheet.Status.DRAFT
    sheet.completed_by = None
    sheet.completed_at = None
    sheet.save()
    AuditEvent.objects.create(
        actor=user, action="grade_sheet_reopened", object_type="GradeSheet", object_id=str(sheet.pk)
    )
    return sheet
