import pytest
from django.urls import reverse

from apps.core.views import EPUB_FILENAME

pytestmark = pytest.mark.django_db


def test_canonical_epub_download_is_public(client):
    response = client.get(reverse("epub-download"))

    try:
        assert response.status_code == 200
        assert response["Content-Type"] == "application/epub+zip"
        assert EPUB_FILENAME in response["Content-Disposition"]
    finally:
        response.close()


def test_legacy_epub_url_delivers_the_canonical_file(client):
    response = client.get(reverse("epub-download-legacy"))

    try:
        assert response.status_code == 200
        assert EPUB_FILENAME in response["Content-Disposition"]
    finally:
        response.close()
