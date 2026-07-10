from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render

from .demo_data import DEMO_DASHBOARD


def health(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status": "ok"})


@login_required
def home(request):
    return render(request, "core/home.html", {"dashboard": DEMO_DASHBOARD})
