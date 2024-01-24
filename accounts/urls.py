# urls.py
from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    # path("my-template/", MyTemplateView.as_view(), name="my_template"),
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # other paths...
]
