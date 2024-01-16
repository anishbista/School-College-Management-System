from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", StudentDashboardView.as_view(), name="student_dashboard"),
]
