from django.urls import path
from .views import *

app_name = "parent"

urlpatterns = [
    path("dashboard/", ParentDashboardView.as_view(), name="parent_dashboard"),
]
