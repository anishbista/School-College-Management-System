from django.contrib import admin
from .models import Assignment, Attendance


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "start", "end", "image", "teacher"]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "course_class",
        "student",
    ]
