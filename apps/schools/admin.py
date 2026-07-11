from django.contrib import admin

from .models import ReportPeriod, School, SchoolYear


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "city")


@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "start_date", "end_date", "is_active")
    list_filter = ("school", "is_active")


@admin.register(ReportPeriod)
class ReportPeriodAdmin(admin.ModelAdmin):
    list_display = ("name", "school_year", "start_date", "end_date", "status")
    list_filter = ("status", "school_year__school")
