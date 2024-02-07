from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(libraryBook)
class libraryBookAdmin(admin.ModelAdmin):
    list_display=['name','author','availability_status']
@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display=['book','borrowed_person','borrowing_date','due_date']
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'address', 'contact_number')
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_number', 'capacity', 'drive_by')
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'start_location', 'end_location')
@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('stop_name', 'route', 'stop_order')
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('bus', 'route', 'day_of_week', 'departure_time', 'arrival_time')
@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('route', 'alert_type', 'alert_message', 'alert_time')