from django import forms
from .models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["name", "description", "start", "end", "image", "hw_file"]
