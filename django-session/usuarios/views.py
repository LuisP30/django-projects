from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from hashlib import sha256

def login(request):
    status = request.GET.get('status') 
    return render(request, 'login.html', context={'status': status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect(f'{reverse("usuarios:login")}?status=1')
    elif len(usuario) > 0:
        request.session['status'] = {'logado': True, 'usuario_id': usuario[0].id}
        return redirect('plataforma:home')

    return HttpResponse(f'{email} {senha}')

# Views para cadastro abaixo:
def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', context={'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip())==0 or len(email.strip())==0:
        return redirect(f"{reverse('usuarios:cadastro')}?status=1")
    if len(senha) < 8:
        return redirect(f"{reverse('usuarios:cadastro')}?status=2")
    
    usuario = Usuario.objects.filter(email = email)
    if len(usuario) > 0:
        return redirect(f"{reverse('usuarios:cadastro')}?status=3")
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(
            nome = nome,
            email = email,
            senha = senha
        )
        usuario.save()
        return redirect(f'{reverse("usuarios:cadastro")}?status=0')
    except:
        return redirect(f'{reverse("usuarios:cadastro")}?status=4')

# View para sair
def sair(request):
    # request.session.clear()
    # O clear apaga todos os dados da minha session e mantém a sessão sem dado nenhum
    # O flush apaga a sessão com todos os dados
    request.session.flush() # Flush é mais recomendável, clear seria recomendável para armazenar carrinho do usuário
    return redirect('usuarios:login')