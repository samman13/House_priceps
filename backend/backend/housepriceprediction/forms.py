from django import forms
from django.contrib.auth.forms import UserCreationForm
# Replace with your custom user model if needed
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Replace with your custom user model if needed
        fields = ['username', 'email', 'password1', 'password2']
