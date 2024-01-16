from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib import messages

from .models import *


# from django.views.generic import TemplateView


# class my_html_view(TemplateView):
#     template_name = "registration/login.html"


class LoginView(View):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            if user.is_active:
                try:
                    student = Student.objects.get(student_userName=user)
                    login(request, user)
                    return redirect(reverse("student_dashboard"))
                except Student.DoesNotExist:
                    pass

                try:
                    teacher = Teacher.objects.get(teacher_userName=user)

                    return redirect(reverse("teacher_dashboard"))
                except Teacher.DoesNotExist:
                    pass
                try:
                    parent = Parent.objects.get(parent_userName=user)
                    return redirect(reverse("parent_dashboard"))
                except Parent.DoesNotExist:
                    pass

            else:
                messages.error(request, "Your account is disabled.")
        else:
            messages.error(request, "Invalid login credentials.")

        return render(request, self.template_name)
