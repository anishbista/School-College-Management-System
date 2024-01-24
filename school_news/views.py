from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
class AnnouncementView(LoginRequiredMixin,View):
    def get(self,request):
        announcements=Announcement.objects.all()
        return render(request,'school_news/announcement.html',{'announcements':announcements})