from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from apps.core import views
from apps.grades import views as grade_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("anmelden/", auth_views.LoginView.as_view(), name="login"),
    path("abmelden/", auth_views.LogoutView.as_view(), name="logout"),
    path("health/", views.health, name="health"),
    path("noten/", grade_views.assignment_list, name="grade-assignment-list"),
    path("noten/<int:assignment_id>/", grade_views.grade_entry, name="grade-entry"),
    path(
        "zeugnis/<int:school_class_id>/<int:period_id>/<int:student_id>/",
        grade_views.report_preview,
        name="report-preview",
    ),
    path("", views.home, name="home"),
]
