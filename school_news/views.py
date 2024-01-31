# from django.shortcuts import render
# from django.views.generic import View, ListView, DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import *
# class AnnouncementView(LoginRequiredMixin, View):
#     active_tab = "announcement"
#     template_name = "students/news/announcement.html"
#     def get(self,request ,*args, **kwargs):
#         announcements=Announcement.objects.all()
#         context={
#             'active_tab':self.active_tab,
#             'announcements':announcements
#         }
#         return render(request,self.template_name,context)
# class EventView(LoginRequiredMixin,View):
#     active_tab = "event"
#     template_name = "students/news/events.html"
#     def get(self,request ,*args, **kwargs):
#         events=Event.objects.all()
#         context={
#             'active_tab':self.active_tab,
#             'events':events
#         }
#         return render(request,self.template_name,context)
# class HolidayView(LoginRequiredMixin,View):
#     active_tab = "holiday"
#     template_name = "students/news/holiday.html"
#     def get(self,request ,*args, **kwargs):
#         holidays=Holiday.objects.all()
#         context={
#             'active_tab':self.active_tab,
#             'holidays':holidays
#         }
#         return render(request,self.template_name,context)