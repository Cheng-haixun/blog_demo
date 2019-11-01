from django import forms
from .models import User

class UserForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=16)
    email = forms.EmailField()
    comment = forms.CharField()