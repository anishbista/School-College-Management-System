from datetime import date
from typing import Any
from django.db.models.query import QuerySet
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

class StudentDashboardView(LoginRequiredMixin, View):
    template_name = "students/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            student = request.user.student
        except Student.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("accounts:login")
        return render(request, self.template_name)


class AssignmentView(LoginRequiredMixin, BaseView, View):
    template_name = "students/assignment/assignment_view.html"
    active_tab = "assignment_view"
    today_date = date.today()

    def get(self, request, *args, **kwargs):
        try:
            student = request.user.student
            assignments = Assignment.objects.filter(course__grade=student.grade)
        except Student.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("accounts:login")
        context = {
            "active_tab": self.active_tab,
            "assignments": assignments,
            "today_date": self.today_date,
        }
        return render(request, self.template_name, context)


class SubmissionView(View):
    template_name = "students/assignment/assignment_submission.html"
    redirect_url = "student:student_assignment"

    def get(self, request, a_id):
        work = get_object_or_404(Assignment, id=a_id)
        student = request.user.student
        initial_data = {"work": work.name, "student": student.student_name}
        form = SubmissionForm(initial=initial_data)
        return render(request, self.template_name, {"form": form})

    def post(self, request, a_id):
        work = get_object_or_404(Assignment, id=a_id)
        student = request.user.student
        existing_submission = Submit.objects.filter(work=work, student=student).first()

        request.POST = request.POST.copy()
        request.POST["work"] = str(work.id)
        request.POST["student"] = str(student.id)

        """
        request.POST = request.POST.copy(): This line creates a shallow copy of the request.POST dictionary. This is done to ensure that the original request.POST dictionary remains unchanged. It's generally a good practice when you need to modify the data.
        
        request.POST["work"] = str(work.id): This line updates the "work" key in the request.POST dictionary. It assigns the string representation (str()) of the work.id to the "work" key. This is important because your form is expecting the "work" value to be a UUID, and str(work.id) provides that UUID in string format.
        """

        form = SubmissionForm(request.POST, request.FILES, instance=existing_submission)
        if form.is_valid():
            form.save()

            # show sucess msg
        else:
            # show error msg
            return render(
                request,
                "students/assignment/assignment_submission.html",
                {"form": form},
            )
        return redirect("student:student_assignment")


class SubmissionListView(LoginRequiredMixin, BaseView, ListView):
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


class CheckSubmittedAssignment(LoginRequiredMixin, DetailView):
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

class AnnouncementView(LoginRequiredMixin, View):
    active_tab = "announcement"
    template_name = "students/news/announcement.html"
    def get(self,request ,*args, **kwargs):
        announcements=Announcement.objects.all()
        context={
            'active_tab':self.active_tab,
            'announcements':announcements
        }
        return render(request,self.template_name,context)
class EventView(LoginRequiredMixin,View):
    active_tab = "event"
    template_name = "students/news/events.html"
    def get(self,request ,*args, **kwargs):
        events=Event.objects.all()
        context={
            'active_tab':self.active_tab,
            'events':events
        }
        return render(request,self.template_name,context)
class HolidayView(LoginRequiredMixin,View):
    active_tab = "holiday"
    template_name = "students/news/holiday.html"
    def get(self,request ,*args, **kwargs):
        holidays=Holiday.objects.all()
        context={
            'active_tab':self.active_tab,
            'holidays':holidays
        }
        return render(request,self.template_name,context)