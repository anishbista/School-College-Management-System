from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *
from school_news.models import *
from gallery.models import *
from .mixins import ParentRequiredMixin
from teacher.models import Attendance
from student.services import *
from staff.models import *

class ParentDashboardView(ParentRequiredMixin, View):
    template_name = "parents/dashboard.html"

    def get(self, request, *args, **kwargs):
        student = request.user.parent.student
        attendance_data = DashboardService.get_attendance_data(student)
        context = {
            "student": student,
            "attendance_data": attendance_data,
        }

        return render(request, self.template_name, context)


class AnnouncementView(ParentRequiredMixin, View):
    active_tab = "announcement"
    template_name = "parents/news/announcement.html"

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        context = {"active_tab": self.active_tab, "announcements": announcements}
        return render(request, self.template_name, context)


class EventView(ParentRequiredMixin, View):
    active_tab = "event"
    template_name = "parents/news/events.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        context = {"active_tab": self.active_tab, "events": events}
        return render(request, self.template_name, context)


class HolidayView(ParentRequiredMixin, View):
    active_tab = "holiday"
    template_name = "parents/news/holiday.html"

    def get(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        context = {"active_tab": self.active_tab, "holidays": holidays}
        return render(request, self.template_name, context)


# class CourseView(LoginRequiredMixin,View):
#     active_tab = "courses"
#     template_name = "teachers/courses/course.html"
#     def get(self,request):
#         try:
#             courses=Course.objects.filter(teacher=request.user.teacher)
#         except:
#             courses=None
#         context={
#             'active_tab':self.active_tab,
#             'courses':courses
#         }
#         return render(request,self.template_name,context)
# class CourseDetailView(LoginRequiredMixin,View):
#     active_tab = "courses"
#     template_name = "teachers/courses/detail.html"
#     def get(self,request,c_id):
#         try:
#             courses=Course.objects.get(id=c_id)
#         except:
#             courses=None
#         context={
#             'active_tab':self.active_tab,
#             'courses':courses
#         }
#         return render(request,self.template_name,context)


class GalleryView(ParentRequiredMixin, View):
    active_tab = "gallery"
    template_name = "parents/gallery/gallery.html"

    def get(self, request):
        gallerys = Gallery.objects.all()
        context = {"active_tab": self.active_tab, "gallerys": gallerys}
        return render(request, self.template_name, context)

class DriverView(ParentRequiredMixin, View):
    active_tab = "driver"
    template_name = "parents/transportation/driver.html"

    def get(self, request):
        drivers = Driver.objects.all()
        context = {"active_tab": self.active_tab, "drivers": drivers}
        return render(request, self.template_name, context)


class BusView(ParentRequiredMixin, View):
    active_tab = "bus"
    template_name = "parents/transportation/bus.html"

    def get(self, request):
        buses = Bus.objects.all()
        context = {"active_tab": self.active_tab, "buses": buses}
        return render(request, self.template_name, context)


class RouteView(ParentRequiredMixin, View):
    active_tab = "route"
    template_name = "parents/transportation/route.html"

    def get(self, request):
        routes = Route.objects.all()
        context = {"active_tab": self.active_tab, "routes": routes}
        return render(request, self.template_name, context)


class StopView(ParentRequiredMixin, View):
    active_tab = "stop"
    template_name = "parents/transportation/stop.html"

    def get(self, request):
        stops = Stop.objects.all()
        context = {"active_tab": self.active_tab, "stops": stops}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get("stopquery")
        stops = Stop.objects.filter(stop_name__icontains=query)
        context = {"active_tab": self.active_tab, "stops": stops}
        return render(request, self.template_name, context)


class ScheduleView(ParentRequiredMixin, View):
    active_tab = "schedule"
    template_name = "parents/transportation/schedule.html"

    def get(self, request):
        schedules = Schedule.objects.all()
        context = {"active_tab": self.active_tab, "schedules": schedules}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get("schedulequery")
        schedules = Schedule.objects.filter(route__route_name__icontains=query)
        context = {"active_tab": self.active_tab, "schedules": schedules}
        return render(request, self.template_name, context)


class AlertView(ParentRequiredMixin, View):
    active_tab = "alert"
    template_name = "parents/transportation/alert.html"

    def get(self, request):
        alerts = Alert.objects.all()
        context = {"active_tab": self.active_tab, "alerts": alerts}
        return render(request, self.template_name, context)

#college fee
class FeeView(ParentRequiredMixin,View):
    active_tab = "fee"
    template_name = "parents/college_fee/fee.html"
    def get(self,request):
        fees=Fee.objects.all()
        context={
            "active_tab": self.active_tab,
            "fees":fees
        }
        return render(request,self.template_name,context)
class PaymentView(ParentRequiredMixin,View):
    active_tab = "payment"
    template_name = "parents/college_fee/payment_list.html"
    def get(self,request):
        payments=Payment.objects.filter(student=request.user.parent.student)
        context={
            "active_tab": self.active_tab,
            "payments":payments
        }
        return render(request,self.template_name,context)