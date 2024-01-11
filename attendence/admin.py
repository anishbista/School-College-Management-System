from django.contrib import admin
from .models import AbsentStudent
# Register your models here.
@admin.register(AbsentStudent)
class AbsentStudentAdmin(admin.ModelAdmin):
    list_display=['sub_class','date','is_absent']