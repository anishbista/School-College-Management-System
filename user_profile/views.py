from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from accounts.models import *
from .forms import *


class StudentDetailView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentDetailForm
    te
