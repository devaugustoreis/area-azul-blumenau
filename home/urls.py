from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('esqueci_senha/', views.esqueci_senha, name='esqueci_senha'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('como_funciona/', views.como_funciona, name='como_funciona')
]
