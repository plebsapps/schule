from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from apps.classes.models import SchoolClass
from apps.schools.models import ReportPeriod, School


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name="subjects", verbose_name="Schule")
    name = models.CharField("Bezeichnung", max_length=120)
    short_name = models.CharField("Kurzbezeichnung", max_length=20)
    sort_order = models.PositiveSmallIntegerField("Reihenfolge", default=0)
    is_mandatory = models.BooleanField("Pflichtfach", default=True)
    show_on_report = models.BooleanField("Auf Zeugnis anzeigen", default=True)
    grade_min = models.DecimalField("Kleinste Note", max_digits=4, decimal_places=2, default=Decimal("1.00"))
    grade_max = models.DecimalField("Größte Note", max_digits=4, decimal_places=2, default=Decimal("6.00"))
    grade_step = models.DecimalField(
        "Schrittweite",
        max_digits=4,
        decimal_places=2,
        default=Decimal("0.50"),
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    is_active = models.BooleanField("Aktiv", default=True)

    class Meta:
        verbose_name = "Fach"
        verbose_name_plural = "Fächer"
        ordering = ("sort_order", "name")
        constraints = [models.UniqueConstraint(fields=("school", "short_name"), name="unique_subject_short_name")]

    def __str__(self):
        return f"{self.short_name} – {self.name}"

    def clean(self):
        if self.grade_min is not None and self.grade_max is not None and self.grade_min >= self.grade_max:
            raise ValidationError({"grade_max": "Die größte Note muss über der kleinsten Note liegen."})


class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="teaching_assignments",
        verbose_name="Lehrperson",
    )
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.PROTECT, related_name="teaching_assignments", verbose_name="Klasse"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT, related_name="teaching_assignments", verbose_name="Fach"
    )
    report_period = models.ForeignKey(
        ReportPeriod, on_delete=models.PROTECT, related_name="teaching_assignments", verbose_name="Zeugnisperiode"
    )

    class Meta:
        verbose_name = "Unterrichtszuordnung"
        verbose_name_plural = "Unterrichtszuordnungen"
        ordering = ("school_class", "subject", "teacher")
        constraints = [
            models.UniqueConstraint(
                fields=("teacher", "school_class", "subject", "report_period"),
                name="unique_teaching_assignment",
            )
        ]

    def __str__(self):
        return f"{self.school_class} – {self.subject.short_name} – {self.teacher}"

    def clean(self):
        errors = {}
        if self.school_class_id and self.subject_id:
            if self.school_class.school_year.school_id != self.subject.school_id:
                errors["subject"] = "Fach und Klasse müssen derselben Schule angehören."
        if self.school_class_id and self.report_period_id:
            if self.school_class.school_year_id != self.report_period.school_year_id:
                errors["report_period"] = "Klasse und Zeugnisperiode müssen zum selben Schuljahr gehören."
        if errors:
            raise ValidationError(errors)
