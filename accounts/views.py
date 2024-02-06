from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout, views
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
        user = request.user

        if user.is_authenticated:
            if user.is_staff:
                return redirect("http://127.0.0.1:8000/admin")
            user_attributes = ["student", "teacher", "parent","staff"]
            for attribute in user_attributes:
                if hasattr(user, attribute):
                    return redirect(reverse(f"{attribute}:{attribute}_dashboard"))

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            if user.is_active:
                if user.is_staff:
                    login(request, user)
                    print("to superuser")
                    return redirect("http://127.0.0.1:8000/admin")
                user_attributes = ["student", "teacher", "parent","staff"]
                for attribute in user_attributes:
                    if hasattr(user, attribute):
                        login(request, user)
                        return redirect(reverse(f"{attribute}:{attribute}_dashboard"))
            else:
                messages.error(request, "Your account is disabled.")
        else:
            messages.error(request, "Invalid login credentials.")

        return render(request, self.template_name)


class LogoutView(View):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        # return render(request, self.template_name)
        return redirect(reverse("login"))


class CustomPasswordResetView(views.PasswordResetView):
    template_name = "registration/forgot_password.html"
    email_template_name = "registration/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")
