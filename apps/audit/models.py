from django.conf import settings
from django.db import models


class AuditEvent(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Benutzer")
    action = models.CharField("Aktion", max_length=80)
    object_type = models.CharField("Objekttyp", max_length=80)
    object_id = models.CharField("Objekt-ID", max_length=80)
    old_values = models.JSONField("Alte Werte", default=dict)
    new_values = models.JSONField("Neue Werte", default=dict)
    created_at = models.DateTimeField("Zeitpunkt", auto_now_add=True)

    class Meta:
        verbose_name = "Audit-Ereignis"
        verbose_name_plural = "Audit-Ereignisse"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.action} – {self.object_type} {self.object_id}"
