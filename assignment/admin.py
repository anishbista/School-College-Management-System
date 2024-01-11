from django.contrib import admin
from .models import Assignment,Submit,Feedback
# Register your models here.
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display=['name','description','start','end','teacher']
@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display=['work','student']
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['fk_work','fk']