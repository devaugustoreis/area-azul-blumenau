from django.shortcuts import render

def index(request):
    return render(request, "cliente/index.html")

def estacionar(request):
    return render(request, "cliente/estacionar.html")

def extrato(request):
    return render(request, "cliente/extrato.html")

def creditos(request):
    return render(request, "cliente/add_creditos.html")

def multas(request):
    return render(request, "cliente/pagar_nr.html")

def veiculos(request):
    return render(request, "cliente/veiculos.html")

def dados(request):
    return render(request, "cliente/dados.html")