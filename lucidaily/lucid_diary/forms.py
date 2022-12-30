from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
    	'class': 'form-control rounded-left',
    	'placeholder': 'Username'
    }))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
    	'class': 'form-control rounded-left',
    	'placeholder': 'E-mail'
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
    	'class': 'form-control rounded-left',
    	'placeholder': 'Password'
    }))

    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
    	'class': 'form-control rounded-left',
    	'placeholder': 'Password again'
    }))

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


        


class AuthenticationUserForm(AuthenticationForm):

    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
    	'class': 'form-control rounded-left',
    	'placeholder': 'Username'
    }))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
    	'class': 'form-control rounded-left',
    	'placeholder': 'Password'
    }))