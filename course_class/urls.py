from django.urls import path
from .views import CourseView,TimeTableView
app_name="course_class"
urlpatterns=[
    path('subject/',CourseView.as_view(),name='subject'),
    path('timetable/',TimeTableView.as_view(),name='timetable'),
]