from django.shortcuts import render
from django.views import View
from .models import Course,TimeTable
# Create your views here.
class CourseView(View):
    def get(self,request):
        courses=Course.objects.all()
        return render(request,'course_class/subject.html',{'courses':courses,'subject':'active'})
class TimeTableView(View):
    def get(self,request):
        timetable=TimeTable.objects.all()
        return render(request,'course_class/timetable.html',{'timetable':timetable,'tt':'active'})

