from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def esqueci_senha(request):
    return render(request, 'home/esqueci_senha.html')