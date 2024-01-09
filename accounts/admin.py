from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SchoolUser)
class SchoolUserAdmin(admin.ModelAdmin):
    list_display=['user','role']
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=['level','department']
admin.site.register(Department)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_user','department','grade']