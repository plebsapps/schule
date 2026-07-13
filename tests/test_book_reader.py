import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import Client
from django.urls import reverse

from apps.accounts.models import BOOK_READER_GROUP_NAME

SYNTHETIC_BOOK_PASSWORD = "Synthetic-Book-Password-1!"


@pytest.mark.django_db
def test_ensure_book_reader_creates_read_only_user():
    call_command("ensure_book_reader", password=SYNTHETIC_BOOK_PASSWORD)

    user = get_user_model().objects.get(username="Buch")
    assert user.is_active is True
    assert user.is_staff is True
    assert user.is_superuser is False
    assert user.role == user.Role.SUBJECT_TEACHER
    assert user.must_change_password is False
    assert user.check_password(SYNTHETIC_BOOK_PASSWORD) is True
    assert user.groups.filter(name=BOOK_READER_GROUP_NAME).exists() is True


@pytest.mark.django_db
def test_ensure_book_reader_is_idempotent_and_keeps_single_user():
    call_command("ensure_book_reader", password=SYNTHETIC_BOOK_PASSWORD)
    call_command("ensure_book_reader", password=SYNTHETIC_BOOK_PASSWORD)

    assert get_user_model().objects.filter(username="Buch").count() == 1
    assert get_user_model().objects.get(username="Buch").groups.filter(name=BOOK_READER_GROUP_NAME).count() == 1


@pytest.mark.django_db
def test_book_reader_can_view_admin_but_not_edit():
    call_command("ensure_book_reader", password=SYNTHETIC_BOOK_PASSWORD)
    user = get_user_model().objects.get(username="Buch")
    client = Client()
    client.force_login(user)

    changelist = client.get(reverse("admin:schools_school_changelist"), HTTP_HOST="schule.plebsapps.de", secure=True)
    add_view = client.get(reverse("admin:schools_school_add"), HTTP_HOST="schule.plebsapps.de", secure=True)

    assert changelist.status_code == 200
    assert add_view.status_code == 403


@pytest.mark.django_db
def test_book_reader_cannot_change_own_password():
    call_command("ensure_book_reader", password=SYNTHETIC_BOOK_PASSWORD)
    user = get_user_model().objects.get(username="Buch")
    client = Client()
    client.force_login(user)

    password_change_url = reverse("admin:password_change")
    password_change_get = client.get(password_change_url, HTTP_HOST="schule.plebsapps.de", secure=True)
    password_change_post = client.post(
        password_change_url,
        {
            "old_password": SYNTHETIC_BOOK_PASSWORD,
            "new_password1": "Synthetic-New-Password-1!",
            "new_password2": "Synthetic-New-Password-1!",
        },
        HTTP_HOST="schule.plebsapps.de",
        secure=True,
    )
    direct_password_change = client.get(
        reverse("admin:auth_user_password_change", args=(user.pk,)),
        HTTP_HOST="schule.plebsapps.de",
        secure=True,
    )
    admin_index = client.get(reverse("admin:index"), HTTP_HOST="schule.plebsapps.de", secure=True)

    user.refresh_from_db()
    assert password_change_get.status_code == 403
    assert password_change_post.status_code == 403
    assert direct_password_change.status_code == 403
    assert user.check_password(SYNTHETIC_BOOK_PASSWORD) is True
    assert password_change_url not in admin_index.content.decode()
    assert user.can_change_own_password is False


@pytest.mark.django_db
def test_administrator_can_still_change_password():
    administrator = get_user_model().objects.create_superuser(
        username="admin-password-test",
        password="Synthetic-Admin-Password-1!",
    )
    client = Client()
    client.force_login(administrator)

    response = client.get(
        reverse("admin:password_change"),
        HTTP_HOST="schule.plebsapps.de",
        secure=True,
    )

    assert response.status_code == 200
    assert administrator.can_change_own_password is True
