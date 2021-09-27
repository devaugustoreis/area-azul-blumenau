from django.urls import path
from . import views

urlpatterns = [
    path("<str:pk>/", views.index, name="index"),
    path("estacionar/<str:pk>/", views.estacionar, name="estacionar"),
    path("extrato/<str:pk>/", views.extrato, name="extrato"),
    path("creditos/<str:pk>/", views.creditos, name="creditos"),
    path("multas/<str:pk>/", views.multas, name="multas"),
    path("veiculos/<str:pk>/", views.veiculos, name="veiculos"),
    path("dados/<str:pk>/", views.dados, name="dados"),
]