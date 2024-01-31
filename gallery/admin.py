from django.contrib import admin
from .models import Gallery
# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['name','description','date']