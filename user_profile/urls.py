from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = "user_profile"

urlpatterns = [
    path(
        "",
        StudentDetailView.as_view(),
        name="profile",
    ),
]
