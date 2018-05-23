from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,)