from django.contrib import admin

from .models import ClassEnrollment, Student


class ClassEnrollmentInline(admin.TabularInline):
    model = ClassEnrollment
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "last_name", "first_name", "birth_date", "school", "is_active")
    list_filter = ("school", "is_active")
    search_fields = ("student_number", "last_name", "first_name")
    inlines = (ClassEnrollmentInline,)


@admin.register(ClassEnrollment)
class ClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "school_class", "entry_date", "exit_date")
    list_filter = ("school_class__school_year", "school_class")
    search_fields = ("student__student_number", "student__last_name", "student__first_name")
