from django.shortcuts import render

def login(request):
    return render(request, 'home/login.html')

def esqueci_senha(request):
    return render(request, 'home/esqueci_senha.html')