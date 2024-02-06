from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import View
from .mixins import StaffRequiredMixin
from school_news.models import *
from gallery.models import *
from .models import libraryBook, Borrowing
from .forms import BorrowingForm, LibraryBookForm


class StaffDashboardView(StaffRequiredMixin, View):
    template_name = "staffs/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )


class AnnouncementView(StaffRequiredMixin, View):
    active_tab = "announcement"
    template_name = "staffs/news/announcement.html"

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        context = {"active_tab": self.active_tab, "announcements": announcements}
        return render(request, self.template_name, context)


class EventView(StaffRequiredMixin, View):
    active_tab = "event"
    template_name = "staffs/news/events.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        context = {"active_tab": self.active_tab, "events": events}
        return render(request, self.template_name, context)


class HolidayView(StaffRequiredMixin, View):
    active_tab = "holiday"
    template_name = "staffs/news/holiday.html"

    def get(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        context = {"active_tab": self.active_tab, "holidays": holidays}
        return render(request, self.template_name, context)


class GalleryView(StaffRequiredMixin, View):
    active_tab = "gallery"
    template_name = "staffs/gallery/gallery.html"

    def get(self, request):
        gallerys = Gallery.objects.all()
        context = {"active_tab": self.active_tab, "gallerys": gallerys}
        return render(request, self.template_name, context)


class libraryBookView(StaffRequiredMixin, View):
    active_tab = "librarybook"
    template_name = "staffs/library/booklist.html"

    def get(self, request):
        books = libraryBook.objects.all()
        context = {"active_tab": self.active_tab, "books": books}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get("bookquery")
        print(query)
        books = libraryBook.objects.filter(name__icontains=query)
        context = {"active_tab": self.active_tab, "books": books}
        return render(request, self.template_name, context)


class BorrowedView(StaffRequiredMixin, View):
    active_tab = "borrowed"
    template_name = "staffs/library/borrowedlist.html"

    def get(self, request):
        borrowlist = Borrowing.objects.all()
        context = {"active_tab": self.active_tab, "borrowlist": borrowlist}
        return render(request, self.template_name, context)


class LendBookView(StaffRequiredMixin, View):
    template_name = "staffs/library/lendbook.html"

    def get(self, request, b_id):
        form = BorrowingForm(book_id=b_id)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, b_id):
        form = BorrowingForm(request.POST, book_id=b_id)
        if form.is_valid():
            form.save()
            return redirect("staff:librarybook")
        context = {"form": form}
        return render(request, self.template_name, context)


class ReturnBook(StaffRequiredMixin, View):
    def get(self, request, borrow_id):
        try:
            Borrow = Borrowing.objects.get(id=borrow_id)
            Borrow.delete()
            return redirect("staff:librarybook")
        except:
            return redirect("staff:dashboard")


class AddBook(StaffRequiredMixin, View):
    active_tab = "addbook"
    template_name = "staffs/library/addbook.html"

    def get(self, request):
        form = LibraryBookForm()
        context = {"active_tab": self.active_tab, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = LibraryBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff:librarybook")
        context = {"active_tab": self.active_tab, "form": form}
        return render(request, self.template_name, context)
