from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", ParentDashboardView.as_view(), name="parent_dashboard"),
]
