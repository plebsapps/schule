from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.accounts.models import BOOK_READER_GROUP_NAME

READ_ONLY_PERMISSION_NAMES = (
    ("schools", "school"),
    ("schools", "schoolyear"),
    ("schools", "reportperiod"),
    ("classes", "schoolclass"),
    ("students", "student"),
    ("students", "classenrollment"),
    ("subjects", "subject"),
    ("subjects", "teachingassignment"),
    ("reports", "reporttemplate"),
    ("grades", "gradesheet"),
    ("grades", "grade"),
    ("audit", "auditevent"),
)


class Command(BaseCommand):
    help = "Erstellt oder aktualisiert das Lesekonto für das Praxislehrbuch."

    def add_arguments(self, parser):
        parser.add_argument(
            "--password",
            required=True,
            help="Neues Passwort für den Benutzer 'Buch'. Es wird nicht im Repository gespeichert.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        password = options["password"]
        if not password:
            raise CommandError("Ein Passwort muss angegeben werden.")

        user_model = get_user_model()
        user, _ = user_model.objects.update_or_create(
            username="Buch",
            defaults={
                "first_name": "Buch",
                "last_name": "Lesekonto",
                "email": "buch@example.invalid",
                "is_active": True,
                "is_staff": True,
                "is_superuser": False,
                "role": user_model.Role.SUBJECT_TEACHER,
                "must_change_password": False,
            },
        )
        user.set_password(password)
        user.save(update_fields=("password",))

        group, _ = Group.objects.get_or_create(name=BOOK_READER_GROUP_NAME)
        permissions = []
        for app_label, model_name in READ_ONLY_PERMISSION_NAMES:
            permission = Permission.objects.get(codename=f"view_{model_name}", content_type__app_label=app_label)
            permissions.append(permission)
        group.permissions.set(permissions)
        user.groups.set([group])
        user.user_permissions.clear()

        self.stdout.write(
            self.style.SUCCESS(
                "Lesekonto 'Buch' aktualisiert. Passwort wurde gesetzt und Read-only-Gruppe zugewiesen."
            )
        )
