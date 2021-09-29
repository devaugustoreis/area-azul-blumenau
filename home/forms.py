from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class CreateUser(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


# class SignUpForm(forms.ModelForm):
#     CPF = forms.CharField(max_length=9, required=True)
#     birth_date = forms.DateField(required=True)
#     phone1 = forms.CharField(max_length=20, required=True)
#     phone2 = forms.CharField(max_length=20)
#     password = forms.CharField(max_length=15, required=True)
#     password_confirm = forms.CharField(max_length=15, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'email', 'password']

#         def clean(self):
#             cleaned_data = super(SignUpForm, self).clean()
#             password = cleaned_data.get('password')
#             password_confirm = cleaned_data.get('password_confirm')

#             if password != password_confirm:
#                 raise forms.ValidationError('Passwords do not match!')
