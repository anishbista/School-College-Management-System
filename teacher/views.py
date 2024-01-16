from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *


class TeacherDashboardView(LoginRequiredMixin, View):
    template_name = "teachers/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            teacher = request.user.teacher
        except Teacher.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("login")
        return render(request, self.template_name)
