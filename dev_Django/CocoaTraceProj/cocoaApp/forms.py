# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d’utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)