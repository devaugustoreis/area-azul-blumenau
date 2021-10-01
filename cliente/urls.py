from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("estacionar/", views.estacionar, name="estacionar"),
    path("extrato/", views.extrato, name="extrato"),
    path("creditos/", views.creditos, name="creditos"),
    path("multas/", views.multas, name="multas"),
    path("veiculos/", views.veiculos, name="veiculos"),
    path("dados/", views.dados, name="dados"),
    # path("atualizar_dados/", views.atualizarDados, name="atualizar-dados"),
]