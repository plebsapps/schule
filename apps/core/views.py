from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import FileResponse, JsonResponse
from django.shortcuts import render

from .dashboard import build_dashboard

IMAGE_STYLES = (
    {
        "number": "01",
        "name": "Flat Vector",
        "file": "design-01-flat-vector.png",
        "description": "Klar, sachlich und besonders gut für technische Erklärgrafiken.",
    },
    {
        "number": "02",
        "name": "Isometrisch",
        "file": "design-02-isometrisch.png",
        "description": "Räumliche Prozessdarstellung mit hoher visueller Detailwirkung.",
    },
    {
        "number": "03",
        "name": "Schweizer Editorial",
        "file": "design-03-schweizer-editorial.png",
        "description": "Strenges Raster, starke Geometrie und moderner Fachbuchcharakter.",
    },
    {
        "number": "04",
        "name": "Blueprint",
        "file": "design-04-blueprint.png",
        "description": "Technische Blaupause für Architektur- und Ablaufdiagramme.",
    },
    {
        "number": "05",
        "name": "Papiercollage",
        "file": "design-05-papiercollage.png",
        "description": "Haptischer, redaktioneller Stil mit handwerklicher Anmutung.",
    },
    {
        "number": "06",
        "name": "3D Clay",
        "file": "design-06-3d-clay.png",
        "description": "Freundliche dreidimensionale Lernillustration mit weichen Formen.",
    },
    {
        "number": "07",
        "name": "Monoline",
        "file": "design-07-monoline.png",
        "description": "Minimalistische Liniengrafik für ruhige und präzise Abläufe.",
    },
    {
        "number": "08",
        "name": "Dark Tech",
        "file": "design-08-dark-tech.png",
        "description": "Dunkler technischer Stil mit leuchtenden Prüf- und Prozesswegen.",
    },
    {
        "number": "09",
        "name": "Aquarell",
        "file": "design-09-aquarell.png",
        "description": "Menschlicher, erzählerischer Editorial-Stil mit sichtbarer Textur.",
    },
    {
        "number": "10",
        "name": "Geometrisch / Bauhaus",
        "file": "design-10-bauhaus.png",
        "description": "Abstrakte Formensprache mit starkem Wiedererkennungswert.",
    },
)

EPUB_FILENAME = "arbeiten-mit-openai-codex.epub"


def health(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status": "ok"})


def image_style_gallery(request):
    return render(request, "public/image_style_gallery.html", {"styles": IMAGE_STYLES})


def epub_download(request):
    epub_path = settings.BASE_DIR / "static" / "downloads" / EPUB_FILENAME
    return FileResponse(
        open(epub_path, "rb"),
        as_attachment=True,
        filename=EPUB_FILENAME,
        content_type="application/epub+zip",
    )


@login_required
def home(request):
    return render(request, "core/home.html", {"dashboard": build_dashboard(request.user)})
