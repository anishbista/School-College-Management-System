from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *
from school_news.models import *
from gallery.models import *
from .mixins import ParentRequiredMixin


class ParentDashboardView(ParentRequiredMixin, View):
    template_name = "parents/dashboard.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


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
