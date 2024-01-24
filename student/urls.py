from django.urls import path
from .views import *
app_name='student'
urlpatterns = [
    path("dashboard/", StudentDashboardView.as_view(), name="student_dashboard"),
    path('assignment/',AssignmentView.as_view(),name="student_assignment"),
    path('submission/<str:a_id>/',SubmissionView.as_view(),name="submission"),
]
