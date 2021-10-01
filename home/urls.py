from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrar, name='login'),
    path('sair/', views.sair, name='logout'),
    path('esqueci_senha/', views.esqueci_senha, name='esqueci_senha'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('como_funciona/', views.como_funciona, name='como_funciona'),
    path('perguntas_frequentes/', views.perguntas_frequentes, name='perguntas_frequentes'),
    path('contato/', views.contato, name='contato')
]
