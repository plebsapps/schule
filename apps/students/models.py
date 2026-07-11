from django.core.exceptions import ValidationError
from django.db import models

from apps.classes.models import SchoolClass
from apps.schools.models import School


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name="students", verbose_name="Schule")
    student_number = models.CharField("Interne Schülernummer", max_length=50)
    first_name = models.CharField("Vorname", max_length=150)
    last_name = models.CharField("Nachname", max_length=150)
    birth_date = models.DateField("Geburtsdatum")
    entry_date = models.DateField("Eintrittsdatum", blank=True, null=True)
    exit_date = models.DateField("Austrittsdatum", blank=True, null=True)
    is_active = models.BooleanField("Aktiv", default=True)

    class Meta:
        verbose_name = "Schülerin oder Schüler"
        verbose_name_plural = "Schülerinnen und Schüler"
        ordering = ("last_name", "first_name")
        constraints = [models.UniqueConstraint(fields=("school", "student_number"), name="unique_student_number")]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class ClassEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="enrollments", verbose_name="Schüler")
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.PROTECT, related_name="enrollments", verbose_name="Klasse"
    )
    entry_date = models.DateField("Eintritt in die Klasse")
    exit_date = models.DateField("Austritt aus der Klasse", blank=True, null=True)

    class Meta:
        verbose_name = "Klassenzuordnung"
        verbose_name_plural = "Klassenzuordnungen"
        ordering = ("school_class", "student")
        constraints = [
            models.UniqueConstraint(fields=("student", "school_class"), name="unique_student_class_enrollment")
        ]

    def __str__(self):
        return f"{self.student} – {self.school_class}"

    def clean(self):
        errors = {}
        if self.student_id and self.school_class_id:
            if self.student.school_id != self.school_class.school_year.school_id:
                errors["school_class"] = "Schüler und Klasse müssen derselben Schule angehören."
        if self.entry_date and self.exit_date and self.entry_date > self.exit_date:
            errors["exit_date"] = "Der Austritt darf nicht vor dem Eintritt liegen."
        if errors:
            raise ValidationError(errors)
