from django.urls import path
from .views import *
app_name="school_news"
urlpatterns=[
    path('holiday/',HolidayView.as_view(),name="holiday"),
    path('event/',EventView.as_view(),name='event'),
    path('announcement/',AnnouncementView.as_view(),name="announcement"),
]