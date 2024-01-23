from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.utils.timezone import now
from common.base_view import BaseView


class TeacherDashboardView(LoginRequiredMixin, View):
    template_name = "teachers/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            teacher = request.user.teacher
        except Teacher.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("login")
        return render(request, self.template_name)


class AddAssignmentView(LoginRequiredMixin, BaseView, CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teachers/assignment/add_assignment.html"
    success_url = reverse_lazy("list_assignment")
    active_tab = "add_assignment"

    def form_valid(self, form):
        print("Hello")
        form.instance.teacher = self.request.user.teacher

        # print(form.cleaned_data)
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
    success_url = reverse_lazy("list_assignment")
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
        return redirect(
            "list_assignment"
        )  # Replace with the name of the view where you display the assignments


class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "teachers/attendance/attendance_form.html"
    success_url = reverse_lazy("list_assignment")
    active_tab = "attendance_take"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = Teacher.objects.get(teacher_userName=self.request.user)
        course = Course.objects.filter(teacher=teacher)
        request = self.request
        course_id = request.GET.get("course_id")
        if course_id:
            course_object = Course.objects.get(pk=course_id)
            students = course_object.grade.student.all()
            context["students"] = students
        context["courses"] = course

        return context

    # def form_valid(self, form):
    #     # Get the selected students from the form
    #     selected_students_ids = self.request.POST.getlist("status")
    #     print(selected_students_ids)

    #     # Loop through selected students and save attendance for each
    #     for student_id in selected_students_ids:
    #         student = Student.objects.get(pk=student_id)
    #         attendance = form.save(commit=False)
    #         attendance.student = student
    #         attendance.save()

    #     return super().form_valid(form)

    def form_invalid(self, form):
        selected_students_ids = self.request.POST.getlist("status")
        print(selected_students_ids)
        messages.error(
            self.request, "Error creating assignment. Please correct the form."
        )
        print("invalid")
        print("Form data:", form.data)
        print(form.errors)

        return super().form_invalid(form)
