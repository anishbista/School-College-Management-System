from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ParentDashboardView(LoginRequiredMixin, View):
    template_name = "parents/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
