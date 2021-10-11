from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pk>/estacionar/", views.estacionar, name="estacionar"),
    path("<str:pk>/extrato/", views.extrato, name="extrato"),
    path("<str:pk>/creditos/", views.creditos, name="creditos"),
    path("<str:pk>/multas/", views.multas, name="multas"),
    path("<str:pk>/veiculos/", views.veiculos, name="veiculos"),
    # path("<str:pk>/veiculos/adicionar/", views.adicionarVeiculo, name="adicionarVeiculo"),
    path("<str:pk_client>/veiculos/excluir/<str:pk_vehicle>/", views.excluirVeiculo, name="excluirVeiculo"),
    path("<str:pk>/dados/", views.dados, name="dados"),
]