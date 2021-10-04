from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrar, name='login'),
    path('sair/', views.sair, name='logout'),
    path('esqueci_senha/', views.esqueci_senha, name='esqueci_senha'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perguntas_frequentes/', views.perguntas_frequentes, name='perguntas_frequentes'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato')
]
