from django import forms 
from django.contrib.auth.models import User


class Login(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username' , 'password')