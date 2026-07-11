from datetime import date
from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.urls import reverse

from apps.classes.models import SchoolClass
from apps.schools.models import ReportPeriod, School, SchoolYear
from apps.students.models import ClassEnrollment, Student
from apps.subjects.models import Subject, TeachingAssignment


@pytest.fixture
def master_data(db):
    school = School.objects.create(name="Beispielschule")
    school_year = SchoolYear.objects.create(
        school=school,
        name="2026/2027",
        start_date=date(2026, 8, 1),
        end_date=date(2027, 7, 31),
    )
    report_period = ReportPeriod.objects.create(
        school_year=school_year,
        name="1. Halbjahr",
        start_date=date(2026, 8, 1),
        end_date=date(2027, 1, 31),
    )
    teacher = get_user_model().objects.create_user(username="lehrkraft-beispiel")
    school_class = SchoolClass.objects.create(
        school_year=school_year,
        name="7A",
        grade_level="7",
        class_teacher=teacher,
    )
    subject = Subject.objects.create(
        school=school,
        name="Beispielfach",
        short_name="BF",
        grade_min=Decimal("1.00"),
        grade_max=Decimal("6.00"),
        grade_step=Decimal("0.50"),
    )
    student = Student.objects.create(
        school=school,
        student_number="K-0001",
        first_name="Kim",
        last_name="Beispiel",
        birth_date=date(2014, 2, 3),
    )
    return {
        "school": school,
        "school_year": school_year,
        "report_period": report_period,
        "teacher": teacher,
        "school_class": school_class,
        "subject": subject,
        "student": student,
    }


@pytest.mark.django_db
def test_staff_user_can_open_school_management(client):
    user = get_user_model().objects.create_superuser(username="verwaltung", password="rein-kuenstlich-123")
    client.force_login(user)

    response = client.get(reverse("admin:schools_school_changelist"))

    assert response.status_code == 200
    assert "Schule" in response.content.decode()


@pytest.mark.django_db
def test_regular_user_cannot_open_school_management(client):
    user = get_user_model().objects.create_user(username="fachlehrkraft")
    client.force_login(user)

    response = client.get(reverse("admin:schools_school_changelist"))

    assert response.status_code == 302
    assert response.url.startswith(reverse("admin:login"))


@pytest.mark.django_db
def test_staff_status_alone_does_not_grant_school_access(client):
    user = get_user_model().objects.create_user(username="mitarbeiter", is_staff=True)
    client.force_login(user)

    response = client.get(reverse("admin:schools_school_changelist"))

    assert response.status_code == 403


def test_report_period_must_be_inside_school_year(master_data):
    period = ReportPeriod(
        school_year=master_data["school_year"],
        name="Ungültige Periode",
        start_date=date(2026, 7, 1),
        end_date=date(2027, 1, 31),
    )

    with pytest.raises(ValidationError, match="innerhalb des Schuljahres"):
        period.full_clean()


def test_enrollment_requires_same_school(master_data):
    other_school = School.objects.create(name="Andere Beispielschule")
    other_year = SchoolYear.objects.create(
        school=other_school,
        name="2026/2027",
        start_date=date(2026, 8, 1),
        end_date=date(2027, 7, 31),
    )
    other_class = SchoolClass.objects.create(school_year=other_year, name="8B", grade_level="8")
    enrollment = ClassEnrollment(student=master_data["student"], school_class=other_class, entry_date=date(2026, 8, 1))

    with pytest.raises(ValidationError, match="derselben Schule"):
        enrollment.full_clean()


def test_teaching_assignment_connects_teacher_class_subject_and_period(master_data):
    assignment = TeachingAssignment(
        teacher=master_data["teacher"],
        school_class=master_data["school_class"],
        subject=master_data["subject"],
        report_period=master_data["report_period"],
    )

    assignment.full_clean()
    assignment.save()

    assert TeachingAssignment.objects.get().teacher == master_data["teacher"]


def test_referenced_school_cannot_be_deleted(master_data):
    with pytest.raises(ProtectedError):
        master_data["school"].delete()
