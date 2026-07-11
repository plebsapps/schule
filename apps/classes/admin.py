from django.contrib import admin

from .models import SchoolClass


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("name", "grade_level", "school_year", "class_teacher", "is_active")
    list_filter = ("school_year", "grade_level", "is_active")
    search_fields = ("name", "class_teacher__first_name", "class_teacher__last_name")
