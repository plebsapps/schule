from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (*BaseUserAdmin.fieldsets, ("Schule", {"fields": ("role", "must_change_password")}))
    add_fieldsets = (*BaseUserAdmin.add_fieldsets, ("Schule", {"fields": ("role", "must_change_password")}))
    list_display = (*BaseUserAdmin.list_display, "role", "must_change_password")
    list_filter = (*BaseUserAdmin.list_filter, "role", "must_change_password")
