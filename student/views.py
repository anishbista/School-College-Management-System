from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import *
from assignment.models import Assignment,Feedback,Submit
from .forms import SubmissionForm
class StudentDashboardView(LoginRequiredMixin, View):
    template_name = "students/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            student = request.user.student
        except Student.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("login")
        return render(request, self.template_name)

class AssignmentView(LoginRequiredMixin,View):
    template_name = "student/assignmentview.html"
    def get(self,request,*args, **kwargs):
        try:
            student = request.user.student
            assigments=Assignment.objects.filter(grade=student.grade)
        except Student.DoesNotExist:
            messages.error(request, "You don't have permission to access this page")
            return redirect("accounts:login")
        return render(request,self.template_name,{'assignments':assigments})
class SubmissionView(View):
    def get(self,request,a_id):
        work = get_object_or_404(Assignment, id=a_id)
        student = request.user.student
        initial_data = {'work': work, 'student': student}
        form = SubmissionForm(initial=initial_data)
        return render(request, 'student/submissionform.html', {'form': form})
    def post(self,request,a_id):
        work = get_object_or_404(Assignment, id=a_id)
        student = request.user.student        
        existing_submission = Submit.objects.filter(work=work, student=student).first()
        if existing_submission:
            form = SubmissionForm(request.POST, request.FILES, instance=existing_submission)
            if form.is_valid():
                submission = form.save()
            else:
                pass
        else:
            form = SubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                submission = form.save(commit=False)
                submission.work = work
                submission.student = student
                submission.save()
                #show sucess msg
            else:
                #show error msg
                return render(request, 'student/submissionform.html', {'form': form})
        return redirect('student:student_assignment')