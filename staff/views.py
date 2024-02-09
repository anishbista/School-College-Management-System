from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View
from .mixins import StaffRequiredMixin
from school_news.models import *
from gallery.models import *
from .models import libraryBook, Borrowing
from .forms import BorrowingForm, LibraryBookForm,AlertForm,FeeForm,PaymentForm,ExamForm
from .services import *


class StaffDashboardView(StaffRequiredMixin, View):
    template_name = "staffs/dashboard.html"

    def get(self, request, *args, **kwargs):
        available_books = LibraryService.get_total_available_books()
        overdue_books = LibraryService.get_total_overdue_books()
        added_books = LibraryService.get_recently_added_books()
        for i in added_books:
            print(i)
        context = {
            "available_books": available_books,
            "overdue_books": overdue_books,
            "added_books": added_books,
        }

        return render(request, self.template_name, context)


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
class AlertView(StaffRequiredMixin, View):
    active_tab = "alert"
    template_name = "staffs/transportation/alert.html"

    def get(self, request):
        alerts = Alert.objects.all()
        context = {"active_tab": self.active_tab, "alerts": alerts}
        return render(request, self.template_name, context)
class DeleteAlert(StaffRequiredMixin,View):
    def get(self,request,a_id):
        try:
            alert=Alert.objects.get(id=a_id)
            alert.delete()
            return redirect("staff:alert")
        except:
            return redirect("staff:alert")
class EditAlertView(StaffRequiredMixin,View):
    active_tab = "alert"
    template_name = "staffs/transportation/edit_alert.html"
    def get(self,request,a_id):
        alert=get_object_or_404(Alert, id=a_id)
        form=AlertForm(instance=alert)
        context={
            "active_tab": self.active_tab,
            "form":form,
            "a_id":a_id,
        }
        return render(request,self.template_name,context)
    def post(self,request,a_id):
        alert=get_object_or_404(Alert, id=a_id)
        form=AlertForm(request.POST,instance=alert)
        if form.is_valid():
            form.save()
            return redirect("staff:alert")
        else:
            context={
            "active_tab": self.active_tab,
            "form":form,
            "a_id":a_id,
            }
            return render(request,self.template_name,context)
class AddAlertView(StaffRequiredMixin,View):
    active_tab = "alert"
    template_name = "staffs/transportation/add_alert.html"
    def get(self,request):
        form=AlertForm()
        context={
            "active_tab": self.active_tab,
            "form":form,
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form=AlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff:alert")
        else:
            context={
            "active_tab": self.active_tab,
            "form":form,
            }
            return render(request,self.template_name,context)
#college fee
class FeeView(StaffRequiredMixin,View):
    active_tab = "fee"
    template_name = "staffs/college_fee/fee.html"
    def get(self,request):
        fees=Fee.objects.all()
        context={
            "active_tab": self.active_tab,
            "fees":fees
        }
        return render(request,self.template_name,context)
class PaymentView(StaffRequiredMixin,View):
    active_tab = "payment"
    template_name = "staffs/college_fee/payment_list.html"
    def get(self,request):
        payments=Payment.objects.all()
        context={
            "active_tab": self.active_tab,
            "payments":payments
        }
        return render(request,self.template_name,context)
class AddFeeView(StaffRequiredMixin,View):
    active_tab = "fee"
    template_name = "staffs/college_fee/add_fee.html"
    def get(self,request):
        form=FeeForm()
        context={
            "active_tab": self.active_tab,
            "form":form,   
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form=FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff:feelist")
        else:
            context={
            "active_tab": self.active_tab,
            "form":form,   
        }
        return render(request,self.template_name,context)
class AddPaymentView(StaffRequiredMixin,View):
    active_tab="payment"
    template_name = "staffs/college_fee/add_payment.html"
    def get(self,request):
        form=PaymentForm()
        context={
            "active_tab": self.active_tab,
            "form":form,   
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form=PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff:payment")
        else:
            context={
            "active_tab": self.active_tab,
            "form":form,   
        }
        return render(request,self.template_name,context)
#exam
class ExamListView(StaffRequiredMixin,View):
    active_tab="exam_list"
    template_name = "staffs/exam/exam_list.html"
    def get(self,request):
        exams=Exam.objects.all()
        context={
            "active_tab": self.active_tab,
            "exams":exams
        }
        return render(request,self.template_name,context)
class AddExamView(StaffRequiredMixin,View):
    active_tab="add_exam"
    template_name = "staffs/exam/add_exam.html"
    def get(self,request):
        form=ExamForm()
        context={
            "active_tab": self.active_tab,
            "form":form
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form=ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff:exam_list")
        else:
            context={
            "active_tab": self.active_tab,
            "form":form
            }
            return render(request,self.template_name,context)
class EditExamView(StaffRequiredMixin,View):
    template_name = "staffs/exam/add_exam.html"
    def get(self,request,e_id):
        exam=get_object_or_404(Exam,id=e_id)
        form=ExamForm(instance=exam)
        context={
            "form":form,
            "e_id":e_id,
        }
        return render(request,self.template_name,context)
    def post(self,request,e_id):
        exam=get_object_or_404(Exam,id=e_id)
        form=ExamForm(request.POST,instance=exam)
        if form.is_valid():
            form.save()
            return redirect("staff:exam_list")
        else:
            context={
            "form":form,
            "e_id":e_id,
            }
            return render(request,self.template_name,context)