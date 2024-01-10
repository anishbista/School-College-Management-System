from django.contrib import admin
from .models import Course,Grade,TimeTable
# Register your models here.

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["level"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "course_name",
        "teacher",
    ]
@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display=['tname','tclass','tcourse','start','end','date']