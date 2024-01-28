from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from accounts.models import *


class ChatBoxView(LoginRequiredMixin, View):
    template_name = "chat/sidebar.html"

    def get_context_data(self, **kwargs):
        context = {}
        teacher = Teacher.objects.get(teacher_userName=self.request.user)
        course = Course.objects.filter(teacher=teacher)
        student = Student.objects.filter(grade__course__in=course)
        context["students"] = student
        for i in student:
            print(i)

        # context[""] =
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class ChatMessageView(LoginRequiredMixin, View):
    template_name = "chat/sidebar.html"

    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        print(student)
        context = {"student": student}
        return render(request, self.template_name, context)
