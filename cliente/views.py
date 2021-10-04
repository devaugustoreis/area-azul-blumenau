from django.http.response import HttpResponse
from home.models import Address, Client, Vehicle
from home.forms import AddressForm, ClientForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def index(request):
    return render(request, "cliente/index.html", {})


@login_required(login_url='login')
def estacionar(request, pk):
    client = Client.objects.get(pk=pk)
    cars = client.vehicle_set.filter(vehicle_type='C')
    motos = client.vehicle_set.filter(vehicle_type='M')
    others = client.vehicle_set.filter(vehicle_type='O')
    vehicles = Vehicle.objects.filter(owners__id=pk)
    
    context = {'client':client, 'cars':cars, 'motos':motos, 'others':others, 'vehicles':vehicles}
    return render(request, "cliente/estacionar.html", context)


@login_required(login_url='login')
def extrato(request, pk):
    client = Client.objects.get(pk=pk)

    return render(request, "cliente/extrato.html", {})


@login_required(login_url='login')
def creditos(request, pk):
    client = Client.objects.get(pk=pk)

    return render(request, "cliente/add_creditos.html", {})


@login_required(login_url='login')
def multas(request, pk):
    client = Client.objects.get(pk=pk)

    return render(request, "cliente/pagar_nr.html", {})


@login_required(login_url='login')
def veiculos(request, pk):
    client = Client.objects.get(pk=pk)
    cars = client.vehicle_set.filter(vehicle_type='C')
    motos = client.vehicle_set.filter(vehicle_type='M')
    others = client.vehicle_set.filter(vehicle_type='O')
    vehicles = Vehicle.objects.filter(owners__id=pk)
    
    context = {'client':client, 'cars':cars, 'motos':motos, 'others':others, 'vehicles':vehicles}
    return render(request, "cliente/veiculos.html", context)


@login_required(login_url='login')
def dados(request, pk):
    client = Client.objects.get(pk=pk)
    address = client.address

    clientForm = ClientForm(instance=client)
    addressForm = AddressForm(instance=address)

    if request.method == 'POST':
        clientForm = ClientForm(request.POST, instance=client)
        addressForm = AddressForm(request.POST, instance=address)
        if clientForm.is_valid() and addressForm.is_valid():
            clientForm.save()
            addressForm.save()

    context = {'clientForm':clientForm, 'addressForm':addressForm}
    return render(request, "cliente/dados.html", context)


@login_required(login_url='login')
def adicionarVeiculo(request, pk):
    client = Client.objects.get(id=pk)

    if request.method == 'POST':
        plate = request.POST['license_plate']
        type = request.POST['vehicle_type']

        newVehicle = Vehicle.objects.create(
            license_plate = plate, 
            vehicle_type = type
        )

        newVehicle.owners.add(client)
        messages.add_message(request, messages.success, 'Carro Cadastrado com Sucesso!')

        return render(request, "cliente/veiculos.html")


@login_required(login_url='login')
def excluirVeiculo(request, pk_client, pk_vehicle):
    client = Client.objects.get(id=pk_client)
    vehicle = Vehicle.objects.get(id=pk_vehicle)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('veiculos', client.pk)

    context = {'vehicle':vehicle}
    return render(request, "cliente/excluir.html", context)