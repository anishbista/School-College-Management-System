from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *
from .models import *
from .forms import *
from django.urls import reverse_lazy


class TeacherDashboardView(LoginRequiredMixin, View):
    template_name = "teachers/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            teacher = request.user.teacher
        except Teacher.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("login")
        return render(request, self.template_name)


class AddAssignmentView(LoginRequiredMixin, CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teachers/assignment/add_assignment.html"
    success_url = reverse_lazy("teacher_dashboard")

    def form_valid(self, form):
        print("Hello")
        form.instance.teacher = self.request.user.teacher

        # print(form.cleaned_data)
        print("Form data:", form.data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid")
        print("Form data:", form.data)
        print(form.errors)

        return super().form_invalid(form)
