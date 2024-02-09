from django.contrib import admin
from .models import *
# library
@admin.register(libraryBook)
class libraryBookAdmin(admin.ModelAdmin):
    list_display=['name','author','availability_status']
@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display=['book','borrowed_person','borrowing_date','due_date']
#transportation
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
#fee
@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('fee_name', 'amount', 'due_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'fee', 'amount_paid', 'payment_date')

#exam
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'start_date', 'status','duration')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'score')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('result', 'text')