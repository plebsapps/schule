import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.urls import reverse

from apps.audit.models import AuditEvent
from apps.grades.models import Grade, GradeSheet
from apps.grades.services import GradeConflictError, reopen_sheet, save_grade_values
from apps.students.models import Student
from apps.subjects.models import TeachingAssignment


@pytest.fixture
def grade_demo(db):
    call_command("create_demo_master_data")
    teacher = get_user_model().objects.get(username="demo-lehrkraft-keine-anmeldung")
    teacher.is_active = True
    teacher.save(update_fields=("is_active",))
    assignment = TeachingAssignment.objects.get(subject__short_name="DEMO-MA")
    students = list(Student.objects.filter(student_number__startswith="DEMO").order_by("student_number"))
    return teacher, assignment, students


def grade_post(students, values, action="save", versions=None):
    data = {"action": action}
    versions = versions or {}
    for student, value in zip(students, values, strict=True):
        data[f"grade_{student.pk}"] = value
        data[f"version_{student.pk}"] = versions.get(student.pk, 0)
    return data


@pytest.mark.django_db
def test_assigned_teacher_can_save_complete_and_view_report(client, grade_demo):
    teacher, assignment, students = grade_demo
    client.force_login(teacher)

    response = client.post(
        reverse("grade-entry", args=(assignment.pk,)),
        grade_post(students, ("2,0", "2,5", "3,0"), action="complete"),
        follow=True,
    )

    assert response.status_code == 200
    assert Grade.objects.count() == 3
    assert GradeSheet.objects.get().status == GradeSheet.Status.COMPLETED
    assert AuditEvent.objects.filter(action="grade_saved").count() == 3
    assert AuditEvent.objects.filter(action="grade_sheet_completed").count() == 1
    assert "abgeschlossen und gesperrt" in response.content.decode()

    preview = client.get(
        reverse("report-preview", args=(assignment.school_class_id, assignment.report_period_id, students[0].pk))
    )
    assert preview.status_code == 200
    assert assignment.subject.name in preview.content.decode()
    assert "Nicht freigegebene Demo-Vorschau" in preview.content.decode()


@pytest.mark.django_db
def test_unassigned_teacher_cannot_open_grade_entry(client, grade_demo):
    _, assignment, _ = grade_demo
    outsider = get_user_model().objects.create_user(username="fremde-lehrkraft")
    client.force_login(outsider)

    response = client.get(reverse("grade-entry", args=(assignment.pk,)))

    assert response.status_code == 403


@pytest.mark.django_db
def test_grade_scale_is_validated(client, grade_demo):
    teacher, assignment, students = grade_demo
    client.force_login(teacher)

    response = client.post(
        reverse("grade-entry", args=(assignment.pk,)),
        grade_post(students, ("2,3", "2,5", "3,0")),
        follow=True,
    )

    assert "Schrittweite" in response.content.decode()
    assert Grade.objects.count() == 0


@pytest.mark.django_db
def test_optimistic_locking_detects_stale_version(grade_demo):
    teacher, assignment, students = grade_demo
    student = students[0]
    save_grade_values(assignment=assignment, user=teacher, values={student.pk: "2.0"}, versions={student.pk: 0})

    with pytest.raises(GradeConflictError):
        save_grade_values(assignment=assignment, user=teacher, values={student.pk: "3.0"}, versions={student.pk: 0})


@pytest.mark.django_db
def test_only_administrator_can_reopen_completed_sheet(grade_demo):
    teacher, assignment, students = grade_demo
    save_grade_values(
        assignment=assignment,
        user=teacher,
        values={student.pk: "2.0" for student in students},
        versions={student.pk: 0 for student in students},
    )
    sheet = GradeSheet.objects.get()
    sheet.status = GradeSheet.Status.COMPLETED
    sheet.save(update_fields=("status",))
    administrator = get_user_model().objects.create_superuser(username="demo-admin", password="rein-kuenstlich-123")

    reopen_sheet(sheet=sheet, user=administrator)

    sheet.refresh_from_db()
    assert sheet.status == GradeSheet.Status.DRAFT
    assert AuditEvent.objects.filter(action="grade_sheet_reopened").exists()
