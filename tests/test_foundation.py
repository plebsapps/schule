import pytest
from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.urls import reverse

from apps.core.demo_data import DEMO_DASHBOARD


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
    assert "Ausschließlich künstliche Beispieldaten" in content
    assert "Lehrkraft Beispiel" in content


@pytest.mark.django_db
def test_demo_dashboard_does_not_create_domain_records(client):
    user = get_user_model().objects.create_user(username="kuenstliche-lehrkraft")
    client.force_login(user)

    client.get(reverse("home"))

    assert get_user_model().objects.count() == 1
    assert DEMO_DASHBOARD["school_year"] == "2026/2027"


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
