from django.urls import path
from .views import *

urlpatterns = [
    path("", TeacherDashboardView.as_view(), name="teacher_dashboard"),
    path("add_assignment/", AddAssignmentView.as_view(), name="add_assignment"),
    path(
        "edit_assignment/<uuid:pk>",
        EditAssignmentView.as_view(),
        name="edit_assignment",
    ),
    path("list_assignment/", ListAssignmentView.as_view(), name="list_assignment"),
    path(
        "delete_assignment/<uuid:assignment_id>",
        DeleteAssignmentView.as_view(),
        name="delete_assignment",
    ),
    path("attendance/", AttendanceCreateView.as_view(), name="attendance"),
]
