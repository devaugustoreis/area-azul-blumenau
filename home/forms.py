from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# class ClientForm(ModelForm):
#     class Meta:
#         model = Client
#         fields = '__all__'


# class CreateUser(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['user', 'first_name', 'last_name', 'phone1', 'phone2', 'email', 'credits', 'password1', 'password2']
