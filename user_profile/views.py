# from django.shortcuts import render
# from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

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
from .forms import PersonalDetailsForm


class StudentDetailView(LoginRequiredMixin, View):
    template_name = "user_profile/profile.html"

    def get(self, request, *args, **kwargs):
        form = PersonalDetailsForm()
        # profile = request.user.teacher
        # print(profile)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = PersonalDetailsForm(request.POST)
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
        return render(request, self.template_name, {"form": form})
