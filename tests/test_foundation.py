import pytest
from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.core.management import call_command
from django.urls import reverse


@pytest.mark.django_db
def test_health_endpoint_checks_database(client):
    response = client.get(reverse("health"))

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_requires_authentication(client):
    response = client.get(reverse("home"))

    assert response.status_code == 302
    assert response.url.startswith(reverse("login"))


@pytest.mark.django_db
def test_authenticated_user_can_open_home(client):
    user = get_user_model().objects.create_user(username="testlehrkraft", password="rein-kuenstlich-123")
    client.force_login(user)

    response = client.get(reverse("home"))

    assert response.status_code == 200
    content = response.content.decode()
    assert "Direkt aus der Datenbank" in content
    assert "Keine zugewiesenen Klassen" in content


@pytest.mark.django_db
def test_superuser_dashboard_uses_persisted_demo_master_data(client):
    call_command("create_demo_master_data")
    user = get_user_model().objects.create_superuser(username="kuenstliche-verwaltung", password="rein-kuenstlich-123")
    client.force_login(user)

    response = client.get(reverse("home"))
    content = response.content.decode()

    assert "DEMO-7A" in content
    assert "DEMO – Beispielschule am Stadtpark" in content
    assert "Meine Beispielklassen" not in content


def test_login_page_uses_local_design_assets(client):
    response = client.get(reverse("login"))
    content = response.content.decode()

    assert response.status_code == 200
    assert 'label for="id_username"' in content
    assert 'label for="id_password"' in content
    assert "https://fonts." not in content
    assert "Keine echten Schülerdaten" in content
    assert finders.find("css/app.css") is not None


def test_custom_user_model_is_configured(settings):
    assert settings.AUTH_USER_MODEL == "accounts.User"


def test_login_lockout_is_configured(settings):
    assert settings.AXES_FAILURE_LIMIT == 5
    assert settings.AXES_LOCKOUT_PARAMETERS == [["username", "ip_address"]]
