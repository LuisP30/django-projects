from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.http import HttpResponse
from .models import *
from hashlib import sha256

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip())==0 or len(email.strip())==0:
        return redirect(f"{reverse('usuarios:login')}?status=1")
    if len(senha) > 8:
        return redirect(f"{reverse('usuarios:login')}?status=2")
    
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email = email)
    if len(usuario) > 0:
        return redirect(f"{reverse('usuarios:login')}?status=3")

    return HttpResponse(f'{nome}, {email}, {senha}')
