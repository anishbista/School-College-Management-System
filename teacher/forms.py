from django import forms
from .models import Assignment, Attendance
from common.models import attendance_choice


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["name", "description", "start", "end", "image", "hw_file"]


class AttendanceForm(forms.ModelForm):
    status = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Attendance
        fields = [
            "course_class",
        ]
