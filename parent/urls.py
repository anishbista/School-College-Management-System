from django.urls import path
from .views import *

app_name = "parent"

urlpatterns = [
    path("dashboard/", ParentDashboardView.as_view(), name="parent_dashboard"),
    path("announcement/", AnnouncementView.as_view(), name="announcement"),
    path("event/", EventView.as_view(), name="event"),
    path("holiday/", HolidayView.as_view(), name="holiday"),
    # path('courses/',CourseView.as_view(),name='courses'),
    # path('courses/<str:c_id>',CourseDetailView.as_view(),name='coursedetail'),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("tansporation/driver/",DriverView.as_view(),name="driver"),
    path("tansporation/bus/",BusView.as_view(),name="bus"),
    path("tansporation/route/",RouteView.as_view(),name="route"),
    path("tansporation/stop/",StopView.as_view(),name="stop"),
    path("tansporation/schedule/",ScheduleView.as_view(),name="schedule"),
    path("tansporation/alert/",AlertView.as_view(),name="alert"),
    path("college/fee/",FeeView.as_view(),name="feelist"),
    path("college/payment/",PaymentView.as_view(),name="payment"),
]
