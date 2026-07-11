from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from apps.accounts.models import User
from apps.classes.models import SchoolClass
from apps.schools.models import ReportPeriod
from apps.students.models import Student
from apps.subjects.models import TeachingAssignment

from .models import Grade, GradeSheet
from .services import GradeConflictError, can_manage_assignment, can_view_class, complete_sheet, save_grade_values


@login_required
def assignment_list(request):
    assignments = TeachingAssignment.objects.select_related("school_class", "subject", "report_period", "teacher")
    if not (request.user.is_superuser or request.user.role in {User.Role.ADMIN, User.Role.SCHOOL_MANAGEMENT}):
        assignments = assignments.filter(Q(teacher=request.user) | Q(school_class__class_teacher=request.user))
    return render(request, "grades/assignment_list.html", {"assignments": assignments.distinct()})


@login_required
def grade_entry(request, assignment_id):
    assignment = get_object_or_404(
        TeachingAssignment.objects.select_related("school_class", "subject", "report_period", "teacher"),
        pk=assignment_id,
    )
    if not can_manage_assignment(request.user, assignment):
        raise PermissionDenied
    students = [enrollment.student for enrollment in assignment.school_class.enrollments.select_related("student")]
    sheet = GradeSheet.objects.filter(assignment=assignment).first()
    grades = {grade.student_id: grade for grade in Grade.objects.filter(sheet=sheet)} if sheet else {}
    if request.method == "POST":
        values = {}
        versions = {}
        for student in students:
            raw_value = request.POST.get(f"grade_{student.pk}", "").strip()
            if raw_value:
                values[student.pk] = raw_value
                versions[student.pk] = int(request.POST.get(f"version_{student.pk}", "0"))
        try:
            sheet = save_grade_values(assignment=assignment, user=request.user, values=values, versions=versions)
            if request.POST.get("action") == "complete":
                complete_sheet(assignment=assignment, user=request.user)
                messages.success(request, "Die Noteneingabe wurde abgeschlossen und gesperrt.")
            else:
                messages.success(request, "Die Noten wurden gespeichert.")
            return redirect("grade-entry", assignment_id=assignment.pk)
        except (ValidationError, GradeConflictError) as exc:
            messages.error(request, str(exc))
    rows = [{"student": student, "grade": grades.get(student.pk)} for student in students]
    return render(request, "grades/entry.html", {"assignment": assignment, "sheet": sheet, "rows": rows})


@login_required
def report_preview(request, school_class_id, period_id, student_id):
    school_class = get_object_or_404(
        SchoolClass.objects.select_related("school_year", "school_year__school"), pk=school_class_id
    )
    period = get_object_or_404(ReportPeriod, pk=period_id, school_year=school_class.school_year)
    student = get_object_or_404(Student, pk=student_id, enrollments__school_class=school_class)
    if not can_view_class(request.user, school_class):
        raise PermissionDenied
    grades = Grade.objects.filter(
        student=student,
        sheet__assignment__school_class=school_class,
        sheet__assignment__report_period=period,
    ).select_related("sheet__assignment__subject")
    return render(
        request,
        "grades/report_preview.html",
        {"school_class": school_class, "period": period, "student": student, "grades": grades},
    )
