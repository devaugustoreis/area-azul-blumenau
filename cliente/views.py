from home.models import Address, Client
from home.forms import AddressForm, ClientForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, "cliente/index.html", {})

@login_required(login_url='login')
def estacionar(request):
    return render(request, "cliente/estacionar.html", {})

@login_required(login_url='login')
def extrato(request):
    return render(request, "cliente/extrato.html", {})

@login_required(login_url='login')
def creditos(request):
    return render(request, "cliente/add_creditos.html", {})

@login_required(login_url='login')
def multas(request):
    return render(request, "cliente/pagar_nr.html", {})

@login_required(login_url='login')
def veiculos(request):
    return render(request, "cliente/veiculos.html", {})

@login_required(login_url='login')
def dados(request):
    clientForm = ClientForm(instance=Client)
    addressForm = AddressForm(instance=Address)

    context = {'clientForm':clientForm, 'addressForm':addressForm}
    return render(request, "cliente/dados.html", context)

# @login_required(login_url='login')
# def atualizarDados(request):
#     clientForm = ClientForm(instance=Client)
#     addressForm = AddressForm(instance=Address)
#     return render(request, "cliente/dados.html", {'cliente': Client, 'clientForm': clientForm, 'addressForm': addressForm})