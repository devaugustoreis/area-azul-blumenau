from home.models import Client
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/index.html", {})

@login_required(login_url='login')
def estacionar(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/estacionar.html", {})

@login_required(login_url='login')
def extrato(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/extrato.html", {})

@login_required(login_url='login')
def creditos(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/add_creditos.html", {})

@login_required(login_url='login')
def multas(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/pagar_nr.html", {})

@login_required(login_url='login')
def veiculos(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/veiculos.html", {})

@login_required(login_url='login')
def dados(request):
    # client = Client.objects.get(id=pk)
    return render(request, "cliente/dados.html", {})