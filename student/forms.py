from django import forms
from assignment.models import Submit
class SubmissionForm(forms.ModelForm):
    class Meta:
        model=Submit
        fields='__all__'
        widgets = {
            'work': forms.TextInput(attrs={'readonly': 'readonly'}),
            'student': forms.TextInput(attrs={'readonly': 'readonly'}),
        }