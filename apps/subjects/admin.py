from django.contrib import admin

from .models import Subject, TeachingAssignment


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("short_name", "name", "school", "sort_order", "is_mandatory", "show_on_report", "is_active")
    list_editable = ("sort_order", "is_mandatory", "show_on_report", "is_active")
    list_filter = ("school", "is_active", "is_mandatory", "show_on_report")
    search_fields = ("name", "short_name")


@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ("school_class", "subject", "teacher", "report_period")
    list_filter = ("report_period", "school_class", "subject")
    search_fields = ("teacher__first_name", "teacher__last_name", "teacher__username")
