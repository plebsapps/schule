from django.db import models

from apps.schools.models import School


class ReportTemplate(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name="report_templates", verbose_name="Schule")
    name = models.CharField("Bezeichnung", max_length=150)
    report_type = models.CharField("Zeugnisart", max_length=100)
    grade_level = models.CharField("Klassenstufe", max_length=20, blank=True)
    template_key = models.SlugField(
        "Vorlagenschlüssel",
        max_length=100,
        help_text="Verweist später auf eine geprüfte, versionierte HTML-Vorlage.",
    )
    version = models.PositiveIntegerField("Version", default=1)
    is_active = models.BooleanField("Aktiv", default=True)

    class Meta:
        verbose_name = "Zeugnisvorlage"
        verbose_name_plural = "Zeugnisvorlagen"
        ordering = ("name", "-version")
        constraints = [
            models.UniqueConstraint(fields=("school", "template_key", "version"), name="unique_report_template_version")
        ]

    def __str__(self):
        return f"{self.name} (v{self.version})"
