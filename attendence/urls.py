from django.urls import path
from .views import AbsentStudentView,AbsentListView
app_name='attendence'
urlpatterns=[
    path('add/',AbsentStudentView.as_view(),name="add"),
    path('list/',AbsentListView.as_view(),name='list'),
]