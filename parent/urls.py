from django.urls import path
from .views import *

app_name = "parent"

urlpatterns = [
    path("dashboard/", ParentDashboardView.as_view(), name="parent_dashboard"),
    path('announcement/',AnnouncementView.as_view(),name='announcement'),
    path('event/',EventView.as_view(),name='event'),
    path('holiday/',HolidayView.as_view(),name='holiday'),
    # path('courses/',CourseView.as_view(),name='courses'),
    # path('courses/<str:c_id>',CourseDetailView.as_view(),name='coursedetail'),
    path('gallery/',GalleryView.as_view(),name="gallery"),
]
