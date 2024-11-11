from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Productcomments

class Commentform(forms.ModelForm):
    class Meta:
        model = Productcomments
        fields = ['text']