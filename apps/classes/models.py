from django.conf import settings
from django.db import models

from apps.schools.models import SchoolYear


class SchoolClass(models.Model):
    school_year = models.ForeignKey(
        SchoolYear, on_delete=models.PROTECT, related_name="classes", verbose_name="Schuljahr"
    )
    name = models.CharField("Bezeichnung", max_length=50)
    grade_level = models.CharField("Klassenstufe", max_length=20)
    class_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="led_classes",
        verbose_name="Klassenlehrperson",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField("Aktiv", default=True)

    class Meta:
        verbose_name = "Klasse"
        verbose_name_plural = "Klassen"
        ordering = ("school_year", "name")
        constraints = [models.UniqueConstraint(fields=("school_year", "name"), name="unique_class_name")]

    def __str__(self):
        return f"{self.name} – {self.school_year.name}"
