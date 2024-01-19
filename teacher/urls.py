from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", TeacherDashboardView.as_view(), name="teacher_dashboard"),
    path("add_assignment/", AddAssignmentView.as_view(), name="add_assignment"),
]
