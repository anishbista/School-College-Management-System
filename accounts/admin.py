from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['role']
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=['level']
admin.site.register(Department)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_user','department','grade','user_role']