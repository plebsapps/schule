from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.accounts.models import User
from apps.classes.models import SchoolClass
from apps.reports.models import ReportTemplate
from apps.schools.models import ReportPeriod, School, SchoolYear
from apps.students.models import ClassEnrollment, Student
from apps.subjects.models import Subject, TeachingAssignment


class Command(BaseCommand):
    help = "Erstellt einen kleinen, vollständig künstlichen Stammdatenbestand."

    @transaction.atomic
    def handle(self, *args, **options):
        school, _ = School.objects.get_or_create(
            name="DEMO – Beispielschule am Stadtpark",
            defaults={
                "street": "Musterweg 1",
                "postal_code": "00000",
                "city": "Beispielstadt",
                "email": "schule@example.invalid",
                "phone": "+49 000 000000",
            },
        )
        school_year, _ = SchoolYear.objects.get_or_create(
            school=school,
            name="2026/2027",
            defaults={"start_date": date(2026, 8, 1), "end_date": date(2027, 7, 31), "is_active": True},
        )
        report_period, _ = ReportPeriod.objects.get_or_create(
            school_year=school_year,
            name="DEMO – 1. Halbjahr",
            defaults={
                "start_date": date(2026, 8, 1),
                "end_date": date(2027, 1, 31),
                "status": ReportPeriod.Status.OPEN,
            },
        )

        teacher, _ = get_user_model().objects.update_or_create(
            username="demo-lehrkraft-keine-anmeldung",
            defaults={
                "first_name": "Lehrkraft",
                "last_name": "Beispiel",
                "email": "lehrkraft@example.invalid",
                "role": User.Role.CLASS_TEACHER,
                "is_active": False,
                "is_staff": False,
            },
        )
        teacher.set_unusable_password()
        teacher.save(update_fields=("password",))

        school_class, _ = SchoolClass.objects.get_or_create(
            school_year=school_year,
            name="DEMO-7A",
            defaults={"grade_level": "7", "class_teacher": teacher},
        )

        subjects = []
        for order, name, short_name in (
            (10, "Deutsch – Beispiel", "DEMO-DE"),
            (20, "Mathematik – Beispiel", "DEMO-MA"),
            (30, "Englisch – Beispiel", "DEMO-EN"),
        ):
            subject, _ = Subject.objects.get_or_create(
                school=school,
                short_name=short_name,
                defaults={
                    "name": name,
                    "sort_order": order,
                    "grade_min": Decimal("1.00"),
                    "grade_max": Decimal("6.00"),
                    "grade_step": Decimal("0.50"),
                },
            )
            subjects.append(subject)
            TeachingAssignment.objects.get_or_create(
                teacher=teacher,
                school_class=school_class,
                subject=subject,
                report_period=report_period,
            )

        for number, first_name, last_name, birth_date in (
            ("DEMO-0001", "Alex", "Muster", date(2013, 9, 12)),
            ("DEMO-0002", "Sam", "Beispiel", date(2014, 1, 23)),
            ("DEMO-0003", "Mika", "Test", date(2013, 11, 5)),
        ):
            student, _ = Student.objects.get_or_create(
                school=school,
                student_number=number,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "birth_date": birth_date,
                    "entry_date": date(2026, 8, 1),
                },
            )
            ClassEnrollment.objects.get_or_create(
                student=student,
                school_class=school_class,
                defaults={"entry_date": date(2026, 8, 1)},
            )

        ReportTemplate.objects.get_or_create(
            school=school,
            template_key="demo-halbjahreszeugnis-klasse-7",
            version=1,
            defaults={
                "name": "DEMO – Halbjahreszeugnis Klasse 7",
                "report_type": "Halbjahreszeugnis",
                "grade_level": "7",
            },
        )

        self.stdout.write(
            self.style.SUCCESS("Künstliche Beispieldaten sind vorhanden: 1 Schule, 1 Klasse, 3 Schüler, 3 Fächer.")
        )
