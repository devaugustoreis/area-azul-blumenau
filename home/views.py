from home.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages

from .models import *
from .forms import *
from .filters import *
from .decorators import *

@unauthenticated_user
def entrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Login ou senha incorretos.')

    context = {}
    return render(request, 'home/login.html', context)


def sair(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def esqueci_senha(request):
    return render(request, 'home/esqueci_senha.html')


@unauthenticated_user
def cadastro(request):
<<<<<<< HEAD
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='Client')
            user.groups.add(group)
            Client.objects.create(
                user=user, name=name, email=email
            )

            messages.success(request, 'Parabéns, ' + name + '. Sua conta foi cadastrada com sucesso!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'home/cadastro.html', context)
=======
    return render(request, 'home/cadastro.html')

def como_funciona(request):
    return render(request, 'home/como_funciona.html')
>>>>>>> 1867436 (Início da página 'Como Funciona')
