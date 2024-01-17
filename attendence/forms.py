from django import forms
from .models import AbsentStudent

class AbsentStudentForm(forms.ModelForm):
    class Meta:
        model = AbsentStudent
        fields = ['absentee', 'sub_class','is_absent']
        widgets = {
            'absentee': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'sub_class': forms.Select(attrs={'class': 'form-control'}),
            'is_absent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }