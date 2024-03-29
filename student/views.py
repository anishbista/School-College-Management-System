from datetime import date
from typing import Any

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from common.base_view import BaseView

# from assignment.models import Assignment, Feedback, Submit
from teacher.models import *
from .models import *
from .forms import SubmissionForm
from school_news.models import *
from gallery.models import *
from .mixins import StudentRequiredMixin
from staff.models import *
from .services import *


class StudentDashboardView(StudentRequiredMixin, View):
    template_name = "students/dashboard.html"

    def get(self, request, *args, **kwargs):
        student = request.user.student
        attendance_data = DashboardService.get_attendance_data(student)
        assignment_data = DashboardService.get_assignment_data(student)

        context = {
            "attendance_data": attendance_data,
            "assignment_data": assignment_data,
        }
        return render(request, self.template_name, context)


class AssignmentView(StudentRequiredMixin, BaseView, View):
    template_name = "students/assignment/assignment_view.html"
    active_tab = "assignment_view"
    today_date = date.today()

    def get(self, request, *args, **kwargs):
        try:
            student = request.user.student
            assignments = Assignment.objects.filter(course__grade=student.grade)
        except Student.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("login")
        context = {
            "active_tab": self.active_tab,
            "assignments": assignments,
            "today_date": self.today_date,
        }
        return render(request, self.template_name, context)


class SubmissionView(StudentRequiredMixin, View):
    template_name = "students/assignment/assignment_submission.html"
    redirect_url = "student:student_assignment"

    def get(self, request, a_id):
        work = get_object_or_404(Assignment, id=a_id)
        student = request.user.student
        print(student.student_userName)
        initial_data = {"work": work.name, "course": work.course.course_name}
        form = SubmissionForm(initial=initial_data)
        return render(request, self.template_name, {"form": form})

    def post(self, request, a_id):
        work = get_object_or_404(Assignment, id=a_id)
        student = request.user.student
        existing_submission = Submit.objects.filter(work=work, student=student).first()

        request.POST = request.POST.copy()
        request.POST["work"] = str(work.id)
        # request.POST["student"] = str(student.id)

        """
        request.POST = request.POST.copy(): This line creates a shallow copy of the request.POST dictionary. This is done to ensure that the original request.POST dictionary remains unchanged. It's generally a good practice when you need to modify the data.
        
        request.POST["work"] = str(work.id): This line updates the "work" key in the request.POST dictionary. It assigns the string representation (str()) of the work.id to the "work" key. This is important because your form is expecting the "work" value to be a UUID, and str(work.id) provides that UUID in string format.
        """

        form = SubmissionForm(request.POST, request.FILES, instance=existing_submission)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = student
            # submission.work = str(work.id)
            submission.save()

        else:

            return render(
                request,
                "students/assignment/assignment_submission.html",
                {"form": form},
            )
        return redirect("student:student_assignment")


class SubmissionListView(StudentRequiredMixin, BaseView, ListView):
    model = Submit
    active_tab = "list_submission"

    template_name = "students/assignment/submission_list.html"
    context_object_name = "submits"
    ordering = ["-created_on"]

    def get_queryset(self):
        print("User:", self.request.user)
        if self.request.user.is_authenticated:
            print("Student:", self.request.user.student)
            queryset = Submit.objects.filter(student=self.request.user.student)
            print("Queryset:", queryset)
            return queryset
        return Submit.objects.none()


class CheckSubmittedAssignment(StudentRequiredMixin, DetailView):
    model = Submit
    active_tab = "list_submission"
    template_name = "students/assignment/checked_assignment.html"

    def get(self, request, *args, **kwargs):
        assignment = self.get_object()
        context = {
            "active_tab": self.active_tab,
            "assignment": assignment,
        }
        return render(request, self.template_name, context)


class AnnouncementView(StudentRequiredMixin, View):
    active_tab = "announcement"
    template_name = "students/news/announcement.html"

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        context = {"active_tab": self.active_tab, "announcements": announcements}
        return render(request, self.template_name, context)


class EventView(StudentRequiredMixin, View):
    active_tab = "event"
    template_name = "students/news/events.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        context = {"active_tab": self.active_tab, "events": events}
        return render(request, self.template_name, context)


class HolidayView(StudentRequiredMixin, View):
    active_tab = "holiday"
    template_name = "students/news/holiday.html"

    def get(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        context = {"active_tab": self.active_tab, "holidays": holidays}
        return render(request, self.template_name, context)


class CourseView(StudentRequiredMixin, View):
    active_tab = "courses"
    template_name = "students/courses/course.html"

    def get(self, request):
        try:
            courses = Course.objects.filter(grade=request.user.student.grade)
        except:
            courses = None
        context = {"active_tab": self.active_tab, "courses": courses}
        return render(request, self.template_name, context)


class CourseDetailView(StudentRequiredMixin, View):
    active_tab = "courses"
    template_name = "students/courses/detail.html"

    def get(self, request, c_id):
        try:
            courses = Course.objects.get(id=c_id)
        except:
            courses = None
        context = {"active_tab": self.active_tab, "courses": courses}
        return render(request, self.template_name, context)


class GalleryView(StudentRequiredMixin, View):
    active_tab = "gallery"
    template_name = "students/gallery/gallery.html"

    def get(self, request):
        gallerys = Gallery.objects.all()
        context = {"active_tab": self.active_tab, "gallerys": gallerys}
        return render(request, self.template_name, context)


class libraryBookView(StudentRequiredMixin, View):
    active_tab = "librarybook"
    template_name = "students/library/booklist.html"

    def get(self, request):
        books = libraryBook.objects.all()
        context = {"active_tab": self.active_tab, "books": books}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get("bookquery")
        books = libraryBook.objects.filter(name__icontains=query)
        context = {"active_tab": self.active_tab, "books": books}
        return render(request, self.template_name, context)


class BorrowedView(StudentRequiredMixin, View):
    active_tab = "borrowed"
    template_name = "students/library/borrowedlist.html"

    def get(self, request):
        borrowlist = Borrowing.objects.filter(borrowed_person=request.user.student)
        context = {"active_tab": self.active_tab, "borrowlist": borrowlist}
        return render(request, self.template_name, context)


class DriverView(StudentRequiredMixin, View):
    active_tab = "driver"
    template_name = "students/transportation/driver.html"

    def get(self, request):
        drivers = Driver.objects.all()
        context = {"active_tab": self.active_tab, "drivers": drivers}
        return render(request, self.template_name, context)


class BusView(StudentRequiredMixin, View):
    active_tab = "bus"
    template_name = "students/transportation/bus.html"

    def get(self, request):
        buses = Bus.objects.all()
        context = {"active_tab": self.active_tab, "buses": buses}
        return render(request, self.template_name, context)


class RouteView(StudentRequiredMixin, View):
    active_tab = "route"
    template_name = "students/transportation/route.html"

    def get(self, request):
        routes = Route.objects.all()
        context = {"active_tab": self.active_tab, "routes": routes}
        return render(request, self.template_name, context)


class StopView(StudentRequiredMixin, View):
    active_tab = "stop"
    template_name = "students/transportation/stop.html"

    def get(self, request):
        stops = Stop.objects.all()
        context = {"active_tab": self.active_tab, "stops": stops}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get("stopquery")
        stops = Stop.objects.filter(stop_name__icontains=query)
        context = {"active_tab": self.active_tab, "stops": stops}
        return render(request, self.template_name, context)


class ScheduleView(StudentRequiredMixin, View):
    active_tab = "schedule"
    template_name = "students/transportation/schedule.html"

    def get(self, request):
        schedules = Schedule.objects.all()
        context = {"active_tab": self.active_tab, "schedules": schedules}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST.get("schedulequery")
        schedules = Schedule.objects.filter(route__route_name__icontains=query)
        context = {"active_tab": self.active_tab, "schedules": schedules}
        return render(request, self.template_name, context)


class AlertView(StudentRequiredMixin, View):
    active_tab = "alert"
    template_name = "students/transportation/alert.html"

    def get(self, request):
        alerts = Alert.objects.all()
        context = {"active_tab": self.active_tab, "alerts": alerts}
        return render(request, self.template_name, context)


# college fee
class FeeView(StudentRequiredMixin, View):
    active_tab = "fee"
    template_name = "students/college_fee/fee.html"

    def get(self, request):
        fees = Fee.objects.all()
        context = {"active_tab": self.active_tab, "fees": fees}
        return render(request, self.template_name, context)


class PaymentView(StudentRequiredMixin, View):
    active_tab = "payment"
    template_name = "students/college_fee/payment_list.html"

    def get(self, request):
        payments = Payment.objects.filter(student=request.user.student)
        context = {"active_tab": self.active_tab, "payments": payments}
        return render(request, self.template_name, context)
