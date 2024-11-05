from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.


def sair(request):
    logout(request)
    return redirect(home)

def home(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # Autentica o usuário
        usu = authenticate(username=usuario, password=senha)

        if usu is not None:
            # Login do usuário
            login(request, usu)

            return render(request, 'base/login.html', {'msg': "credenciado"}) 
        else:
            return render(request, 'base/login.html', {'msg': "Dados incorretos!"})

    return render(request, 'base/login.html', {'msg': ''})

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        contato = request.POST.get('contato')
        senha = request.POST.get('senha')

        # Verifica se o usuário já existe
        if User.objects.filter(username=usuario).exists():
            return render(request, 'base/cadastro.html', {'msg': "Usuário já existe. Tente outro."})

        # Cria um novo superusuário
        User.objects.create_superuser(username=usuario, email=email, password=senha)

        #salvar infor no banco
        Cadastro(usuario=usuario, email=email, contato=contato, senha=senha).save()

        return redirect('home')  # Redireciona para a página de login após o cadastro

    return render(request, 'base/cadastro.html', {'msg': ''})



