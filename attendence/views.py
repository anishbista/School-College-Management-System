from django.shortcuts import render,redirect
from django.views import View
from .forms import AbsentStudentForm
from .models import AbsentStudent
# Create your views here.
class AbsentListView(View):
    def get(self,request):
        absent=AbsentStudent.objects.all()
        absents_stu=AbsentStudent.objects.all().values_list('absentee__student_name', flat=True)
        return render(request,'attendence/absent.html',{'absents':absents_stu})
class AbsentStudentView(View):
    def get(self,request):
        return render(request,'attendence/absentform.html',{'form':AbsentStudentForm()})
    def post(self,request):
        user_abs=AbsentStudentForm(request.POST)
        if user_abs.is_valid():
            user_abs.save()
            user_abs.save_m2m()
            return redirect('attendence:list')
        return render(request,'attendence/absentform.html',{'form':user_abs})
        