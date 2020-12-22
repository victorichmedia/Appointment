from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.urls import reverse
class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30, help_text='Required a valid email address')

    class meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

  