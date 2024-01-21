from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", TeacherDashboardView.as_view(), name="teacher_dashboard"),
    path("add_assignment/", AddAssignmentView.as_view(), name="add_assignment"),
    path(
        "edit_assignment/<uuid:pk>",
        EditAssignmentView.as_view(),
        name="edit_assignment",
    ),
    path("list_assignment/", ListAssignmentView.as_view(), name="list_assignment"),
]
