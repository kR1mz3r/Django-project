from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='ID пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


