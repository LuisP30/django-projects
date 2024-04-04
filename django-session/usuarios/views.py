from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import constants
from .models import *
from django.contrib import messages, auth


def login(request):
    if request.user.is_authenticated:
        return redirect('plataforma:home')
    return render(request, 'login.html')

def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    
    usuario = auth.authenticate(request, username = nome, password = senha)

    if not usuario:
        messages.add_message(request, constants.ERROR , "Usuário ou senha inválidos")
        return redirect("usuarios:login")
    else:
        auth.login(request, usuario)
        messages.add_message(request, constants.INFO, 'Olá seja bem vindo!')
        return redirect('plataforma:home')

# Views para cadastro abaixo:
def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    # Dados pessoais
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    # Dados residenciais
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')

    nome_email_invalidos = False
    senha_invalida = False
    if len(nome.strip())==0 or len(email.strip())==0:
        messages.add_message(request, constants.ERROR, 'Nome e E-mail não podem estar em branco')
        nome_email_invalidos = True
    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no mínimo 8 caracteres')
        senha_invalida = True
    

    if Users.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR, 'E-mail já cadastrado')
        nome_email_invalidos = True

    if Users.objects.filter(username = nome).exists():
        messages.add_message(request, constants.ERROR, 'Nome de usuário já existe')
        nome_email_invalidos = True

    if nome_email_invalidos or senha_invalida:
        return redirect('usuarios:cadastro')
    
    try:
        usuario = Users.objects.create_user(username = nome, email = email, password = senha, cep = cep, rua = rua, numero = numero)
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
        return redirect("usuarios:cadastro")
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect("usuarios:cadastro")

# View para sair
def sair(request):
    auth.logout(request)
    return redirect('usuarios:login')