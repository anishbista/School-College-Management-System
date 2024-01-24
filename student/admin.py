from django.contrib import admin
from .models import *


@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ["work", "student", "teacher", "course"]

    def teacher(self, obj):
        return obj.work.teacher

    def course(self, obj):
        return obj.work.course

    teacher.short_description = "Teacher"
    course.short_description = "Course"
