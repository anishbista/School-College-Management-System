from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

class StudentDetailView(LoginRequiredMixin,UpdateView)