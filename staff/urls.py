from django.urls import path
from .views import *

app_name = "staff"

urlpatterns = [
    path("dashboard/", StaffDashboardView.as_view(), name="staff_dashboard"),
    path("announcement/", AnnouncementView.as_view(), name="announcement"),
    path("event/", EventView.as_view(), name="event"),
    path("holiday/", HolidayView.as_view(), name="holiday"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("library/books/",libraryBookView.as_view(),name="librarybook"),
    path("library/borrowed/",BorrowedView.as_view(),name="borrowed"),
    path("library/addbook/",AddBook.as_view(),name="addbook"),
    path("library/lendbook/<str:b_id>/",LendBookView.as_view(),name="lendbook"),
    path("library/returnbook/<str:borrow_id>/",ReturnBook.as_view(),name="return"),
    path("transportation/alert/",AlertView.as_view(),name="alert"),
    path("transportation/alert/delete/<str:a_id>/",DeleteAlert.as_view(),name="delete_alert"),
    path("transportation/alert/edit/<str:a_id>/",EditAlertView.as_view(),name="edit_alert"),
    path("transportation/alert/add/",AddAlertView.as_view(),name="add_alert"),
]
