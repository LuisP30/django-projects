from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def cadastro(request):
    form = forms.PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio') 


    form = forms.PessoaForm()
    return render(request, 'cadastro.html', context={
        'form': form
    })


def login(request):
    return render(request, 'registration/login.html')

def pessoas(request):
    # pessoas = models.Pessoa.objects.filter(id = 1).filter(nome = 'Luis')  # AND
    pessoas = models.Pessoa.objects.all()
    # pessoas = models.Pessoa.objects.filter(Q(nome = 'Luis') | Q(nome = 'Makarios'))  # OR
    # pessoas = models.Pessoa.objects.filter(Q(nome = 'Luis') | Q(nome = 'Makarios')).exclude(nome = 'Makarios')  # EXCLUDE
    return render(request, 'pessoa.html', context={
        'pessoas': pessoas
    })

@login_required
def perfil(request):
    #pessoa = get_object_or_404(models.Pessoa, id=id)
    form = forms.PessoaForm()
    return render(request, 'perfil.html', context={
        'form': form,
    })

def editar_pessoa(request, id):
    pessoa = models.Pessoa.objects.get(id=id)
    if request.POST:
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.senha = request.POST.get('senha')
        pessoa.save()
        return redirect('autenticacao:pessoas')
    return redirect('autenticacao:pessoas')
    
def excluir_pessoa(request, id):
    if request:
        pessoa = models.Pessoa.objects.filter(id=id).get()
        pessoa.delete()
        return redirect('autenticacao:pessoas')
