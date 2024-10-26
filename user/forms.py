from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(forms.ModelForm):
    # def save(self, commit=True):
    #     user =super().save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user
    
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'password')

class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User

class Resetpassform(forms.Form):
    email= forms.EmailField(label='email', required=True , max_length=30)>