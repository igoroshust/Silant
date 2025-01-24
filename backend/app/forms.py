from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login
from allauth.account.forms import SignupForm
from django import forms
from .models import *

class CustomLogInForm(SignupForm):
    """"""
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.EmailField(label='Почта')

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.set_password = (self.cleaned_data['password'])
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend') # Вход в систему после регистрации
        return user