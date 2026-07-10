from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from apps.core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("anmelden/", auth_views.LoginView.as_view(), name="login"),
    path("abmelden/", auth_views.LogoutView.as_view(), name="logout"),
    path("health/", views.health, name="health"),
    path("", views.home, name="home"),
]
