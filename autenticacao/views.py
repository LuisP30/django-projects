# flake8: noqa
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.db.models import Q

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cargo = request.POST.get('cargo')
        senha = request.POST.get('senha')
        pessoa = models.Pessoa( 
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            senha = senha,
        )
        pessoa.save()
        cargos = models.Cargos.objects.get(id=int(cargo))
        pessoas = models.Pessoa.objects.get(id=pessoa.id)
        pessoas.cargo.add(cargos.id)
        pessoa.save()
        return redirect('autenticacao:pessoas') 

    else:
        return render(request, 'cadastro.html')


def login(request):
    return render(request, 'login.html')

def pessoas(request):
    # pessoas = models.Pessoa.objects.filter(id = 1).filter(nome = 'Luis')  # AND
    pessoas = models.Pessoa.objects.all()
    # pessoas = models.Pessoa.objects.filter(Q(nome = 'Luis') | Q(nome = 'Makarios'))  # OR
    # pessoas = models.Pessoa.objects.filter(Q(nome = 'Luis') | Q(nome = 'Makarios')).exclude(nome = 'Makarios')  # EXCLUDE
    return render(request, 'pessoa.html', context={
        'pessoas': pessoas
    })

def perfil(request, id):
    pessoa = get_object_or_404(models.Pessoa, id=id)
    return render(request, 'perfil.html', context={
        'pessoa': pessoa,
    })

def editar_pessoa(request, id):
    pessoa = models.Pessoa.objects.filter(id=id).get()
    if request.POST:
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.cargo = request.POST.get('cargo')
        pessoa.senha = request.POST.get('senha')
        pessoa.save()
        return redirect('autenticacao:pessoas')
    return redirect('autenticacao:pessoas')
    
def excluir_pessoa(request, id):
    if request:
        pessoa = models.Pessoa.objects.filter(id=id).get()
        pessoa.delete()
        return redirect('autenticacao:pessoas')
