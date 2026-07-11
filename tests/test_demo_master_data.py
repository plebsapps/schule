import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

from apps.classes.models import SchoolClass
from apps.reports.models import ReportTemplate
from apps.schools.models import ReportPeriod, School, SchoolYear
from apps.students.models import ClassEnrollment, Student
from apps.subjects.models import Subject, TeachingAssignment


@pytest.mark.django_db
def test_demo_master_data_is_artificial_complete_and_idempotent():
    call_command("create_demo_master_data")
    call_command("create_demo_master_data")

    school = School.objects.get(name="DEMO – Beispielschule am Stadtpark")
    teacher = get_user_model().objects.get(username="demo-lehrkraft-keine-anmeldung")

    assert school.email.endswith(".invalid")
    assert SchoolYear.objects.filter(school=school).count() == 1
    assert ReportPeriod.objects.filter(school_year__school=school).count() == 1
    assert SchoolClass.objects.filter(school_year__school=school).count() == 1
    assert Student.objects.filter(school=school).count() == 3
    assert ClassEnrollment.objects.filter(student__school=school).count() == 3
    assert Subject.objects.filter(school=school).count() == 3
    assert TeachingAssignment.objects.filter(subject__school=school).count() == 3
    assert ReportTemplate.objects.filter(school=school).count() == 1
    assert teacher.is_active is False
    assert teacher.has_usable_password() is False


@pytest.mark.django_db
def test_demo_command_does_not_change_existing_administrator():
    administrator = get_user_model().objects.create_superuser(
        username="bestehende-verwaltung",
        password="rein-kuenstlich-123",
    )

    call_command("create_demo_master_data")

    administrator.refresh_from_db()
    assert administrator.is_active is True
    assert administrator.is_superuser is True
