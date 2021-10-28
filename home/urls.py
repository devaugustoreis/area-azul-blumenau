from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.entrar, name='login'),
    path('sair/', views.sair, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perguntas_frequentes/', views.perguntas_frequentes, name='perguntas_frequentes'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),

    path('esqueci_senha/', auth_views.PasswordResetView.as_view(template_name='home/esqueci_senha.html'), name='reset_password'),
    path('mudar_senha_solicitação/', auth_views.PasswordResetDoneView.as_view(template_name='home/solicitação_nova_senha.html'), name='password_reset_done'),
    path('mudar_senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/definição_nova_senha.html'), name='password_reset_confirm'),
    path('mudar_senha_completo/', auth_views.PasswordResetCompleteView.as_view(template_name='home/senha_alterada_sucesso.html'), name='password_reset_complete')
]
