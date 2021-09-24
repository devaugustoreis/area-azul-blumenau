from django.shortcuts import render
from .models import *
from .forms import *
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group
# from .decorators import unauthenticated_user, allowed_users, admin_only


# def cadastro(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             id_number = form.cleaned_data['id_number']

#             user.set_password(password)

#             id_model = IdNumber(user.id)
#             id_model.user = user
#             id_model.id_number = id_number

#             id_model.save()
#             form.save()

#             return HttpResponseRedirect('some_url')

#         else:
#             return render(request, 'your_app/your_template.html', {'form': form})

#     else:
#         form = SignUpForm()

#     return render(request, 'your_app/your_template.html', {'form': form}

# @unauthenticated_user
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Usuário ou senha incorretos.')

#     context = {}
#     return render(request, 'accounts/login.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('login')



def login(request):
    return render(request, 'home/login.html')

def esqueci_senha(request):
    return render(request, 'home/esqueci_senha.html')

def cadastro(request):
    return render(request, 'home/cadastro.html')