from django.contrib.staticfiles import finders
from django.urls import reverse

from apps.core.views import IMAGE_STYLES


def test_image_style_gallery_is_public_and_contains_all_designs(client):
    response = client.get(reverse("image-style-gallery"))
    content = response.content.decode()

    assert response.status_code == 200
    assert len(IMAGE_STYLES) == 10
    assert "Arbeiten mit Codex mit GPT-5.6 Sol" in content
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
