from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('esqueci_senha/', views.esqueci_senha, name='esqueci_senha')
]