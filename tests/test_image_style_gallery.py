from django.contrib.staticfiles import finders
from django.urls import reverse

from apps.core.views import IMAGE_STYLES


def test_image_style_gallery_is_public_and_contains_all_designs(client):
    response = client.get(reverse("image-style-gallery"))
    content = response.content.decode()

    assert response.status_code == 200
    assert len(IMAGE_STYLES) == 10
    assert "Arbeiten mit OpenAI Codex" in content
    assert "Praxisbeispiel am Beispiel einer schulischen Zeugnisverwaltung" in content
    assert "Freies Projekt nach GPLv3 auf GitHub" in content
    assert content.count('class="design-card"') == 10
    assert "Flat Vector" in content
    assert "Geometrisch / Bauhaus" in content
    assert "https://" not in content


def test_all_style_preview_assets_are_local():
    for style in IMAGE_STYLES:
        assert finders.find(f"images/style-previews/{style['file']}") is not None


def test_title_cover_asset_is_local():
    assert finders.find("images/book-covers/titelbild-gpt-5-6-sol.png") is not None


def test_title_cover_can_be_downloaded_from_short_public_url(client):
    response = client.get(reverse("title-image-download"))

    assert response.status_code == 200
    assert response["Content-Type"] == "image/png"
    assert 'filename="Titelbild.png"' in response["Content-Disposition"]


def test_publication_text_pdf_can_be_downloaded(client):
    response = client.get(reverse("publication-pdf-download"))

    assert response.status_code == 200
    assert response["Content-Type"] == "application/pdf"
    assert "Ver%C3%B6fentlichungstext.pdf" in response["Content-Disposition"]
