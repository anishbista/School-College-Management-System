from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from school_news.models import *
from gallery.models import *
from .models import libraryBook,Borrowing

class StaffDashboardView(LoginRequiredMixin, View):
    template_name = "staff/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )
class AnnouncementView(LoginRequiredMixin, View):
    active_tab = "announcement"
    template_name = "staff/news/announcement.html"

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        context = {"active_tab": self.active_tab, "announcements": announcements}
        return render(request, self.template_name, context)


class EventView(LoginRequiredMixin, View):
    active_tab = "event"
    template_name = "staff/news/events.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        context = {"active_tab": self.active_tab, "events": events}
        return render(request, self.template_name, context)


class HolidayView(LoginRequiredMixin, View):
    active_tab = "holiday"
    template_name = "staff/news/holiday.html"

    def get(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        context = {"active_tab": self.active_tab, "holidays": holidays}
        return render(request, self.template_name, context)

class GalleryView(LoginRequiredMixin, View):
    active_tab = "gallery"
    template_name = "staff/gallery/gallery.html"

    def get(self, request):
        gallerys = Gallery.objects.all()
        context = {"active_tab": self.active_tab, "gallerys": gallerys}
        return render(request, self.template_name, context)

class libraryBookView(LoginRequiredMixin, View):
    active_tab = "librarybook"
    template_name = "staff/library/booklist.html"

    def get(self, request):
        books=libraryBook.objects.all()
        context = {"active_tab": self.active_tab, "books": books}
        return render(request, self.template_name, context)
    def post(self,request):
        query = request.POST.get('bookquery')
        print(query) 
        books=libraryBook.objects.filter(name__icontains=query)
        context = {"active_tab": self.active_tab, "books": books}
        return render(request, self.template_name, context)

class BorrowedView(LoginRequiredMixin, View):
    active_tab = "borrowed"
    template_name = "staff/library/borrowedlist.html"

    def get(self, request):
        borrowlist=Borrowing.objects.all()
        context = {"active_tab": self.active_tab, "borrowlist": borrowlist}
        return render(request, self.template_name, context)