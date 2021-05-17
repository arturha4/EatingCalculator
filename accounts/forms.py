from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput
from .models import MyCustomUser
from django import forms


class NewUserForm(forms.ModelForm):
    class Meta:
        model=MyCustomUser
        fields=['email','first_name','second_name','password']


class UserLoginForm(forms.Form):
    email=forms.EmailField(label='Логин')
    password=forms.CharField(widget=forms.PasswordInput,label='Пароль')


