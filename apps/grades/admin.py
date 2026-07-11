from django.contrib import admin, messages

from .models import Grade, GradeSheet
from .services import reopen_sheet


@admin.register(GradeSheet)
class GradeSheetAdmin(admin.ModelAdmin):
    list_display = ("assignment", "status", "completed_by", "completed_at")
    list_filter = ("status",)
    actions = ("reopen_selected",)
    readonly_fields = ("assignment", "status", "completed_by", "completed_at")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.action(description="Ausgewählte Noteneingaben wieder öffnen")
    def reopen_selected(self, request, queryset):
        for sheet in queryset:
            reopen_sheet(sheet=sheet, user=request.user)
        self.message_user(request, "Noteneingaben wurden wieder geöffnet.", messages.SUCCESS)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "sheet", "value", "version", "changed_by", "updated_at")
    readonly_fields = ("sheet", "student", "value", "version", "changed_by", "updated_at")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
