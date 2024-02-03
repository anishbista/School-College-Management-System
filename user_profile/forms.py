# from django import forms
# from accounts.models import *


# class StudentDetailForm(forms.ModalForm):
#     class Meta:
#         model = Student
#         fields = ["name", "dob", "email", "address", "phone_no"]


# class TeacherDetailForm(forms.ModalForm):
#     class Meta:
#         model = Student
#         fields = ["name", "dob", "email", "address", "phone_no"]


# class ParentDetailForm(forms.ModalForm):
#     class Meta:
#         model = Student
#         fields = ["name", "dob", "email", "address", "phone_no"]

# forms.py
from django import forms


class PersonalDetailsForm(forms.Form):
    name = forms.CharField(label="Name")
    dob = forms.DateField(label="Date of Birth")
    email = forms.EmailField(label="Email ID")
    phone_no = forms.CharField(label="Mobile")
    address = forms.CharField(label="Address")
    user_type = forms.CharField(label="User Type")
