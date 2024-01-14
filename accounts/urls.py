# urls.py
from django.urls import path
from .views import MyTemplateView

urlpatterns = [
    path("my-template/", MyTemplateView.as_view(), name="my_template"),
    # other paths...
]
