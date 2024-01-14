from django.urls import path
from .views import *
app_name="school_news"
urlpatterns=[
    path('holiday/',HolidayView.as_view(),name="holiday"),
]