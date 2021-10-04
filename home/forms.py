from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'phone1', 'phone2']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class CreateUser(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
