from django.http.response import HttpResponse, HttpResponseRedirect
from home.models import Address, Client, Vehicle, Operation
from home.forms import AddressForm, ClientForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.filters import *


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

    if request.method == 'POST':
        plate = request.POST['license_plate']
        entry = request.POST['entry_time']
        expiration = request.POST['expiration_time']
        creditos = request.POST['value']

        for vehicle in vehicles:
            vehicle.entry_time = None
            vehicle.expiration_time = None
            vehicle.save()

        parkedVehicle = Vehicle.objects.get(license_plate=plate)
        parkedVehicle.entry_time = entry
        parkedVehicle.expiration_time = expiration
        parkedVehicle.save()

        balanco = client.credits
        newBalance = balanco - float(creditos)

        client.credits -= float(creditos)
        client.save()

        Operation.objects.create(
            client=client, operation_type="Estacionar", vehicle=parkedVehicle, value=creditos, balance=newBalance
        )

        return redirect('estacionar', client.pk)
    
    context = {'client':client, 'cars':cars, 'motos':motos, 'others':others, 'vehicles':vehicles}
    return render(request, "cliente/estacionar.html", context)


@login_required(login_url='login')
def extrato(request, pk):
    client = Client.objects.get(pk=pk)
    operations = client.operation_set.all()

    operationFilter = OperationsFilter(request.GET, queryset=operations)
    operations = operationFilter.qs

    context = {'client':client, 'operations':operations, 'operation_filter':operationFilter}
    return render(request, "cliente/extrato.html", context)


@login_required(login_url='login')
def creditos(request, pk):
    client = Client.objects.get(id=pk)

    if request.method == 'POST':
        creditos = request.POST['value']
        operacao = request.POST['operation']
        pagamento = request.POST['payment_method']
        balanco = client.credits
        newBalance = balanco + float(creditos)

        client.credits += float(creditos)
        client.save()

        # messages.add_message(request, messages.SUCCESS, f'R${creditos} em créditos adicionados com sucesso à sua conta!')

        Operation.objects.create(
            client=client, operation_type=operacao, payment_method=pagamento, value=creditos, balance=newBalance
        )

    return render(request, "cliente/adicionar_creditos.html")


# @login_required(login_url='login')
# def multas(request, pk):
#     client = Client.objects.get(pk=pk)

#     return render(request, "cliente/pagar_nr.html", {})


@login_required(login_url='login')
def veiculos(request, pk):
    client = Client.objects.get(pk=pk)
    cars = client.vehicle_set.filter(vehicle_type='C')
    motos = client.vehicle_set.filter(vehicle_type='M')
    others = client.vehicle_set.filter(vehicle_type='O')
    vehicles = Vehicle.objects.filter(owners__id=pk)

    if request.method == 'POST':
        plate = request.POST['license_plate']
        type = request.POST['vehicle_type']

        newVehicle = Vehicle.objects.create(
            license_plate = plate, 
            vehicle_type = type
        )

        newVehicle.owners.add(client)
        # messages.add_message(request, messages.SUCCESS, 'Veículo cadastrado com sucesso!')

        return redirect('veiculos', client.pk)
    
    context = {'client':client, 'cars':cars, 'motos':motos, 'others':others, 'vehicles':vehicles}
    return render(request, "cliente/veiculos.html", context)


# @login_required(login_url='login')
# def adicionarVeiculo(request, pk):
#     client = Client.objects.get(id=pk)

#     if request.method == 'POST':
#         plate = request.POST['license_plate']
#         type = request.POST['vehicle_type']

#         newVehicle = Vehicle.objects.create(
#             license_plate = plate, 
#             vehicle_type = type
#         )

#         newVehicle.owners.add(client)
#         messages.add_message(request, messages.SUCCESS, 'Carro cadastrado com sucesso!')

#         return render(request, "cliente/veiculos.html")


@login_required(login_url='login')
def excluirVeiculo(request, pk_client, pk_vehicle):
    client = Client.objects.get(id=pk_client)
    vehicle = Vehicle.objects.get(id=pk_vehicle)

    if request.method == 'POST':
        vehicle.delete()
        messages.add_message(request, messages.SUCCESS, 'Veículo excluído com sucesso!')

        return redirect('veiculos', client.pk)

    context = {'client':client, 'vehicle':vehicle}
    return render(request, "cliente/excluir.html", context)


@login_required(login_url='login')
def dados(request, pk):
    client = Client.objects.get(pk=pk)
    address = client.address

    clientForm = ClientForm(instance=client)
    addressForm = AddressForm(instance=address)

    if request.method == 'POST':
        clientForm = ClientForm(request.POST, request.FILES, instance=client)
        addressForm = AddressForm(request.POST, instance=address)
        if clientForm.is_valid() and addressForm.is_valid():
            clientForm.save()
            addressForm.save()
            messages.add_message(request, messages.SUCCESS, 'Dados atualizados com sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Um erro ocorreu. Por favor, tente novamente.')


    context = {'client':client, 'clientForm':clientForm, 'addressForm':addressForm}
    return render(request, "cliente/dados.html", context)
