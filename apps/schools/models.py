from django.core.exceptions import ValidationError
from django.db import models


class School(models.Model):
    name = models.CharField("Name", max_length=200)
    street = models.CharField("Straße und Hausnummer", max_length=200, blank=True)
    postal_code = models.CharField("Postleitzahl", max_length=20, blank=True)
    city = models.CharField("Ort", max_length=120, blank=True)
    email = models.EmailField("E-Mail", blank=True)
    phone = models.CharField("Telefon", max_length=50, blank=True)
    is_active = models.BooleanField("Aktiv", default=True)

    class Meta:
        verbose_name = "Schule"
        verbose_name_plural = "Schulen"
        ordering = ("name",)

    def __str__(self):
        return self.name


class SchoolYear(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name="school_years", verbose_name="Schule")
    name = models.CharField("Bezeichnung", max_length=20)
    start_date = models.DateField("Beginn")
    end_date = models.DateField("Ende")
    is_active = models.BooleanField("Aktiv", default=False)

    class Meta:
        verbose_name = "Schuljahr"
        verbose_name_plural = "Schuljahre"
        ordering = ("-start_date",)
        constraints = [models.UniqueConstraint(fields=("school", "name"), name="unique_school_year_name")]

    def __str__(self):
        return f"{self.name} – {self.school}"

    def clean(self):
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError({"end_date": "Das Ende muss nach dem Beginn liegen."})


class ReportPeriod(models.Model):
    class Status(models.TextChoices):
        PREPARATION = "preparation", "Vorbereitung"
        OPEN = "open", "Eingabe geöffnet"
        REVIEW = "review", "Prüfung"
        RELEASED = "released", "Freigegeben"
        COMPLETED = "completed", "Abgeschlossen"
        ARCHIVED = "archived", "Archiviert"

    school_year = models.ForeignKey(
        SchoolYear, on_delete=models.PROTECT, related_name="report_periods", verbose_name="Schuljahr"
    )
    name = models.CharField("Bezeichnung", max_length=100)
    start_date = models.DateField("Beginn")
    end_date = models.DateField("Ende")
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.PREPARATION)

    class Meta:
        verbose_name = "Zeugnisperiode"
        verbose_name_plural = "Zeugnisperioden"
        ordering = ("school_year", "start_date")
        constraints = [models.UniqueConstraint(fields=("school_year", "name"), name="unique_report_period_name")]

    def __str__(self):
        return f"{self.name} – {self.school_year.name}"

    def clean(self):
        errors = {}
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            errors["end_date"] = "Das Ende muss nach dem Beginn liegen."
        if self.school_year_id:
            if self.start_date and self.start_date < self.school_year.start_date:
                errors["start_date"] = "Die Periode muss innerhalb des Schuljahres beginnen."
            if self.end_date and self.end_date > self.school_year.end_date:
                errors["end_date"] = "Die Periode muss innerhalb des Schuljahres enden."
        if errors:
            raise ValidationError(errors)
