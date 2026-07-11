from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from apps.students.models import Student
from apps.subjects.models import TeachingAssignment


class GradeSheet(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "In Bearbeitung"
        COMPLETED = "completed", "Abgeschlossen"

    assignment = models.OneToOneField(
        TeachingAssignment, on_delete=models.PROTECT, related_name="grade_sheet", verbose_name="Unterrichtszuordnung"
    )
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.DRAFT)
    completed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="completed_grade_sheets",
        blank=True,
        null=True,
        verbose_name="Abgeschlossen von",
    )
    completed_at = models.DateTimeField("Abgeschlossen am", blank=True, null=True)

    class Meta:
        verbose_name = "Noteneingabe"
        verbose_name_plural = "Noteneingaben"

    def __str__(self):
        return str(self.assignment)


class Grade(models.Model):
    sheet = models.ForeignKey(GradeSheet, on_delete=models.PROTECT, related_name="grades", verbose_name="Noteneingabe")
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="grades", verbose_name="Schüler")
    value = models.DecimalField("Note", max_digits=4, decimal_places=2)
    version = models.PositiveIntegerField("Version", default=1)
    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="changed_grades", verbose_name="Geändert von"
    )
    updated_at = models.DateTimeField("Geändert am", auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Noten"
        ordering = ("student__last_name", "student__first_name")
        constraints = [models.UniqueConstraint(fields=("sheet", "student"), name="unique_grade_per_sheet_student")]

    def __str__(self):
        return f"{self.student}: {self.value}"

    def clean(self):
        subject = self.sheet.assignment.subject
        if self.value < subject.grade_min or self.value > subject.grade_max:
            raise ValidationError(
                {"value": f"Die Note muss zwischen {subject.grade_min} und {subject.grade_max} liegen."}
            )
        steps = (self.value - subject.grade_min) / subject.grade_step
        if steps != steps.to_integral_value():
            raise ValidationError({"value": f"Die Note muss der Schrittweite {subject.grade_step} entsprechen."})
