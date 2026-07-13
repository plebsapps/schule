from django.contrib.auth.models import AbstractUser
from django.db import models

BOOK_READER_GROUP_NAME = "Buch-Leserecht"


class User(AbstractUser):
    """Benutzerkonto und schulische Rolle einer Mitarbeiterin oder eines Mitarbeiters."""

    class Role(models.TextChoices):
        ADMIN = "admin", "Administration"
        SCHOOL_MANAGEMENT = "school_management", "Schulleitung"
        CLASS_TEACHER = "class_teacher", "Klassenlehrperson"
        SUBJECT_TEACHER = "subject_teacher", "Fachlehrperson"

    role = models.CharField("Rolle", max_length=32, choices=Role.choices, default=Role.SUBJECT_TEACHER)
    must_change_password = models.BooleanField("Passwortänderung erforderlich", default=True)

    @property
    def can_change_own_password(self) -> bool:
        if not self.is_authenticated:
            return False
        return not self.groups.filter(name=BOOK_READER_GROUP_NAME).exists()
