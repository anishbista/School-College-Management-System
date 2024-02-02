from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = "user_profile"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="user_profile/profile.html"),
        name="profile",
    ),
]
