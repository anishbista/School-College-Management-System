from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display=['name','type','start','end']
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=['name','descriptions','start']
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display=['name','descriptions']
