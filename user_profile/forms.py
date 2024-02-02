from django import forms
from accounts.models import *


class StudentDetailForm(forms.ModalForm):
    class Meta:
        model = Student
        fields = ["name", "dob", "email", "address", "phone_no"]


class TeacherDetailForm(forms.ModalForm):
    class Meta:
        model = Student
        fields = ["name", "dob", "email", "address", "phone_no"]


class ParentDetailForm(forms.ModalForm):
    class Meta:
        model = Student
        fields = ["name", "dob", "email", "address", "phone_no"]
