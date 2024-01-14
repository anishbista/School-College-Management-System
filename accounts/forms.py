from django import forms
from common.models import *


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    role = forms.CharField(label="Role", widget=forms.Select(choices=r_choices))
