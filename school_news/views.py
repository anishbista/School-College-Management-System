from django.shortcuts import render
from django.views import View
from .models import Holiday,Announcement,Event
from django.http import HttpResponse
# Create your views here.
class HolidayView(View):
    def get(self,request):
        holidays=Holiday.objects.all()
        return render(request,'school_news/holiday.html',{'holidays':holidays,'day':'active'})
class EventView(View):
    def get(self,request):
        event=Event.objects.all()
        return render(request,'school_news/event.html',{'eve':'active','event':event})