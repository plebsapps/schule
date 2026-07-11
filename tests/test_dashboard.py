import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.urls import reverse

from apps.accounts.models import User
from apps.classes.models import SchoolClass


@pytest.mark.django_db
def test_assigned_teacher_sees_own_class(client):
    call_command("create_demo_master_data")
    teacher = get_user_model().objects.get(username="demo-lehrkraft-keine-anmeldung")
    teacher.is_active = True
    teacher.save(update_fields=("is_active",))
    client.force_login(teacher)

    response = client.get(reverse("home"))
    content = response.content.decode()

    assert response.status_code == 200
    assert "DEMO-7A" in content
    assert "Meine Zuordnungen" in content
    assert ">3<" in content


@pytest.mark.django_db
def test_unassigned_teacher_does_not_see_other_classes(client):
    call_command("create_demo_master_data")
    teacher = get_user_model().objects.create_user(username="nicht-zugewiesen", role=User.Role.SUBJECT_TEACHER)
    client.force_login(teacher)

    response = client.get(reverse("home"))
    content = response.content.decode()

    assert response.status_code == 200
    assert "DEMO-7A" not in content
    assert "DEMO – Beispielschule am Stadtpark" not in content
    assert "Für dieses Konto sind noch keine Klassen zugeordnet" in content


@pytest.mark.django_db
def test_school_management_role_sees_all_classes(client):
    call_command("create_demo_master_data")
    manager = get_user_model().objects.create_user(username="schulleitung", role=User.Role.SCHOOL_MANAGEMENT)
    client.force_login(manager)

    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "DEMO-7A" in response.content.decode()
    assert SchoolClass.objects.count() == 1
