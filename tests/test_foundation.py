import pytest
from django.contrib.auth import get_user_model
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
    assert "Die Anmeldung funktioniert" in response.content.decode()


def test_custom_user_model_is_configured(settings):
    assert settings.AUTH_USER_MODEL == "accounts.User"


def test_login_lockout_is_configured(settings):
    assert settings.AXES_FAILURE_LIMIT == 5
    assert settings.AXES_LOCKOUT_PARAMETERS == [["username", "ip_address"]]
