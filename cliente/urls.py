from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("estacionar/<str:pk>/", views.estacionar, name="estacionar"),
    path("extrato/<str:pk>/", views.extrato, name="extrato"),
    path("creditos/<str:pk>/", views.creditos, name="creditos"),
    path("multas/<str:pk>/", views.multas, name="multas"),
    path("veiculos/<str:pk>/", views.veiculos, name="veiculos"),
    path("dados/<str:pk>/", views.dados, name="dados"),
    path("veiculos/<str:pk>/adicionar/", views.adicionarVeiculo, name="adicionarVeiculo"),
    path("veiculos/<str:pk_client>/excluir/<str:pk_vehicle>/", views.excluirVeiculo, name="excluirVeiculo"),
]