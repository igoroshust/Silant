from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login
from django import forms
from .models import *

class SearchForm(forms.Form):
    """Поиск сведений о машине"""
    query = forms.CharField(label='Поиск', max_length=100)