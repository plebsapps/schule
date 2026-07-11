from django.contrib import admin

from .models import ReportTemplate


@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "report_type", "grade_level", "school", "version", "is_active")
    list_filter = ("school", "report_type", "grade_level", "is_active")
    search_fields = ("name", "template_key")
