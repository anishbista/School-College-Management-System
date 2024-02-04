# from django.shortcuts import render
# from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


# from django.views.generic import UpdateView


# class StudentDetailView(LoginRequiredMixin, View):
#     template_name = "user_profile/profile.html"

#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             self.template_name,
#         )

# views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import PersonalDetailsForm, ChangePasswordForm


class StudentDetailView(LoginRequiredMixin, View):
    template_name = "user_profile/profile.html"

    def get(self, request, *args, **kwargs):

        change_password_form = ChangePasswordForm()
        # profile = request.user.teacher
        # print(profile)

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = PersonalDetailsForm(request.POST)
        change_password_form = ChangePasswordForm(request.POST)
        if form.is_valid():
            print("Hello")
            user_type = form.cleaned_data["user_type"]
            print(user_type)
            # Update user's personal details here
            # Assuming you have a UserProfile model, update the fields accordingly
            profile = getattr(request.user, user_type)
            print(profile)
            profile.name = form.cleaned_data["name"]
            profile.dob = form.cleaned_data["dob"]
            profile.email = form.cleaned_data["email"]
            profile.phone_no = form.cleaned_data["phone_no"]
            profile.address = form.cleaned_data["address"]
            profile.save()
            return redirect("user_profile:profile")

        if change_password_form.is_valid():
            old_password = change_password_form.cleaned_data["old_password"]
            new_password = change_password_form.cleaned_data["new_password"]
            confirm_password = change_password_form.cleaned_data["confirm_password"]
            print(old_password)

            try:
                validate_password(new_password, user=request.user)
            except ValidationError as e:
                messages.error(request, "\n".join(e.messages))
                return render(request, self.template_name)
            result = request.user.check_password(old_password)
            print(result)
            if request:
                if new_password == confirm_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    update_session_auth_hash(
                        request, request.user
                    )  # update_session_auth_hash: This function takes two arguments – the request object and the user object. It is responsible for updating the session with the user's current authentication hash.This is typically done after changing sensitive information related to user authentication, such as updating the password.
                    messages.success(request, "Password changed successfully")
                    logout(request)
                    return redirect("login")
                else:
                    messages.error(request, "Password didn't match.")
            else:
                messages.error(request, "Old Password is incorrect")

            return render(request, self.template_name)
