from django.urls import path
from .views import *

app_name = "chat"

urlpatterns = [
    path("", ChatBoxView.as_view(), name="chat_box"),
    path("student/<uuid:pk>/chat", ChatMessageView.as_view(), name="chat_message"),
]
