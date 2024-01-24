from django.urls import path
from .views import AnnouncementView
app_name='school_news'

urlpatterns=[
    path('announcement/',AnnouncementView.as_view(),name='announcement'),
]