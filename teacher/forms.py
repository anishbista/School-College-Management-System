from django import forms
from .models import Assignment, Attendance


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["name", "description", "start", "end", "image", "hw_file"]


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"
