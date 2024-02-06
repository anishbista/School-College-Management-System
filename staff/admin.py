from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(libraryBook)
class libraryBookAdmin(admin.ModelAdmin):
    list_display=['name','author','availability_status']
@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display=['book','borrowed_person','borrowing_date','due_date']