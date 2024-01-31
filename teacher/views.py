import datetime
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from django.views.generic import View, CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from student.models import Submit
from common.base_view import BaseView
from school_news.models import *
from gallery.models import *

class TeacherDashboardView(LoginRequiredMixin, View):
    template_name = "teachers/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            teacher = request.user.teacher
        except Teacher.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("accounts:login")
        return render(request, self.template_name)


class AddAssignmentView(LoginRequiredMixin, BaseView, CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teachers/assignment/add_assignment.html"
    success_url = reverse_lazy("teacher:list_assignment")
    active_tab = "add_assignment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = Teacher.objects.get(teacher_userName=self.request.user)
        course = Course.objects.filter(teacher=teacher)
        context["courses"] = course
        return context

    def form_valid(self, form):
        print("Hello")
        form.instance.teacher = self.request.user.teacher
        print("Form data:", form.data)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Error creating assignment. Please correct the form."
        )
        print("invalid")
        print("Form data:", form.data)
        print(form.errors)

        return super().form_invalid(form)


class EditAssignmentView(LoginRequiredMixin, BaseView, UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teachers/assignment/edit_assignment.html"
    success_url = reverse_lazy("teacher:list_assignment")
    active_tab = "list_assignment"

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["initial"]["start"] = self.object.start.strftime("%Y-%m-%d")
    #     kwargs["initial"]["end"] = self.object.end.strftime("%Y-%m-%d")
    #     return kwargs

    def get_initial(self):
        initial = super().get_initial()
        assignment = self.get_object()
        initial["start"] = assignment.start.strftime("%Y-%m-%d")
        initial["end"] = assignment.end.strftime("%Y-%m-%d")
        initial["image"] = assignment.image
        initial["hw_file"] = assignment.hw_file
        return initial

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        print("Form data:", form.data)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Error creating assignment. Please correct the form."
        )
        print("invalid")
        print("Form data:", form.data)
        print(form.errors)

        return super().form_invalid(form)


class ListAssignmentView(LoginRequiredMixin, BaseView, ListView):
    model = Assignment
    active_tab = "list_assignment"

    template_name = "teachers/assignment/list_assignment.html"
    context_object_name = "assignments"
    ordering = ["-created_on"]

    def get_queryset(self):
        return Assignment.objects.filter(teacher=self.request.user.teacher)


# class DeleteAssignmentView(LoginRequiredMixin, DeleteView):
#     model = Assignment
#     template_name = "teachers/assignment/delete_assignment.html"
#     success_url = reverse_lazy("list_assignment")


class DeleteAssignmentView(View):
    def get(self, request, assignment_id):
        assignment = get_object_or_404(Assignment, id=assignment_id)
        assignment.delete()
        return redirect("teacher:list_assignment")


class AttendanceCreateView(LoginRequiredMixin, View):
    template_name = "teachers/attendance/attendance_form.html"
    success_url = reverse_lazy("teacher:list_assignment")

    def get_context_data(self, **kwargs):
        context = {}
        teacher = Teacher.objects.get(teacher_userName=self.request.user)
        course = Course.objects.filter(teacher=teacher)
        request = self.request
        course_id = request.GET.get("course_id")
        if course_id:
            course_object = Course.objects.get(pk=course_id)
            students = course_object.grade.student.all()
            context["students"] = students
        context["courses"] = course
        context["active_tab"] = "attendance_take"
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get("course_id")
        if not course_id:
            return redirect(reverse("teacher:attendance"))
        course_object = Course.objects.get(pk=course_id)

        teacher = Teacher.objects.get(teacher_userName=self.request.user)

        date = datetime.date.today()

        present_student_ids = request.POST.getlist("present")

        attendance, created = Attendance.objects.get_or_create(
            teacher=teacher, course_class=course_object, date=date
        )

        if not created:
            messages.error(
                request,
                "Attendance already taken for the day!!",
            )
            return redirect(reverse("teacher:attendance"))

        attendance.present_student.set(present_student_ids)

        return redirect(self.success_url)


class SubmittedAssignment(LoginRequiredMixin, BaseView, ListView):
    template_name = "teachers/assignment/submitted_assignment.html"
    context_object_name = "assignments"
    active_tab = "submitted_assignment"

    def get_queryset(self):
        return Submit.objects.filter(work__teacher=self.request.user.teacher)

    # def get(self, request, *args, **kwargs):
    #     try:
    #         teacher = request.user.teacher
    #         submitted_assignments = Submit.objects.filter(work__teacher=teacher)
    #     except Teacher.DoesNotExist:
    #         messages.error(request, "You don't have permission to access this page")
    #         return redirect("accounts:login")
    #     context = {"active_tab": self.active_tab, "assignments": submitted_assignments}
    #     return render(
    #         request,
    #         self.template_name,
    #         context,
    #     )


class SubmittedAssignmentDetailView(LoginRequiredMixin, DetailView):
    model = Submit
    active_tab = "submitted_assignment"
    template_name = "teachers/assignment/submitted_assignment_detail.html"

    def get(self, request, *args, **kwargs):
        assignment = self.get_object()
        context = {
            "active_tab": self.active_tab,
            "assignment": assignment,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        assignment = self.get_object()

        feedback = request.POST.get("feedback", "")
        checked = "checkAssignment" in request.POST

        assignment.feedback = feedback
        assignment.checked = checked
        assignment.save()
        return redirect("teacher:submitted_assignment")

class AnnouncementView(LoginRequiredMixin, View):
    active_tab = "announcement"
    template_name = "teachers/news/announcement.html"
    def get(self,request ,*args, **kwargs):
        announcements=Announcement.objects.all()
        context={
            'active_tab':self.active_tab,
            'announcements':announcements
        }
        return render(request,self.template_name,context)
class EventView(LoginRequiredMixin,View):
    active_tab = "event"
    template_name="teachers/news/events.html"
    def get(self,request ,*args, **kwargs):
        events=Event.objects.all()
        context={
            'active_tab':self.active_tab,
            'events':events
        }
        return render(request,self.template_name,context)
class HolidayView(LoginRequiredMixin,View):
    active_tab = "holiday"
    template_name = "teachers/news/holiday.html"
    def get(self,request ,*args, **kwargs):
        holidays=Holiday.objects.all()
        context={
            'active_tab':self.active_tab,
            'holidays':holidays
        }
        return render(request,self.template_name,context)

class CourseView(LoginRequiredMixin,View):
    active_tab = "courses"
    template_name = "teachers/courses/course.html"
    def get(self,request):
        try:
            courses=Course.objects.filter(teacher=request.user.teacher)
        except:
            courses=None
        context={
            'active_tab':self.active_tab,
            'courses':courses
        }
        return render(request,self.template_name,context)
class CourseDetailView(LoginRequiredMixin,View):
    active_tab = "courses"
    template_name = "teachers/courses/detail.html"
    def get(self,request,c_id):
        try:
            courses=Course.objects.get(id=c_id)
        except:
            courses=None
        context={
            'active_tab':self.active_tab,
            'courses':courses
        }
        return render(request,self.template_name,context)

class GalleryView(LoginRequiredMixin,View):
    active_tab = "gallery"
    template_name = "teachers/gallery/gallery.html"
    def get(self,request):
        gallerys=Gallery.objects.all()
        context={
            'active_tab':self.active_tab,
            'gallerys':gallerys
        }
        return render(request,self.template_name,context)
