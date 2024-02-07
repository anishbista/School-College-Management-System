from django.urls import path
from .views import *

app_name = "student"

urlpatterns = [
    path("dashboard/", StudentDashboardView.as_view(), name="student_dashboard"),
    path("assignment/", AssignmentView.as_view(), name="student_assignment"),
    path("submission/<str:a_id>/", SubmissionView.as_view(), name="submission"),
    path("submission_list/", SubmissionListView.as_view(), name="submission_list"),
    path(
        "check_assignment/<uuid:pk>",
        CheckSubmittedAssignment.as_view(),
        name="checked_assignment",
    ),
    path("announcement/", AnnouncementView.as_view(), name="announcement"),
    path("event/", EventView.as_view(), name="event"),
    path("holiday/", HolidayView.as_view(), name="holiday"),
    path("courses/", CourseView.as_view(), name="courses"),
    path("courses/<str:c_id>", CourseDetailView.as_view(), name="coursedetail"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("library/books/",libraryBookView.as_view(),name="librarybook"),
    path("library/borrowed/",BorrowedView.as_view(),name="borrowed"),
    path("tansporation/driver/",DriverView.as_view(),name="driver"),
    path("tansporation/bus/",BusView.as_view(),name="bus"),
    path("tansporation/route/",RouteView.as_view(),name="route"),
    path("tansporation/stop/",StopView.as_view(),name="stop"),
    path("tansporation/schedule/",ScheduleView.as_view(),name="schedule"),
    path("tansporation/alert/",AlertView.as_view(),name="alert"),
]
