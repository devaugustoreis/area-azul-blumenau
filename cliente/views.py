from home.models import Client
from django.shortcuts import render

def index(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/index.html", {'client': client})

def estacionar(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/estacionar.html", {'client': client})

def extrato(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/extrato.html", {'client': client})

def creditos(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/add_creditos.html", {'client': client})

def multas(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/pagar_nr.html", {'client': client})

def veiculos(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/veiculos.html", {'client': client})

def dados(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "cliente/dados.html", {'client': client})