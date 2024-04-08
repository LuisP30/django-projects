from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url = 'usuarios:login')
def home(request):
    if request.method == 'GET':
        form = Cliente()
        return render(request, 'home.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = Cliente(request.POST)
        # form.data['nome'] acessando o campo nome do formulário recebeido
        print(form.is_valid())
        if form.is_valid():
            nome = form.data['nome']
            idade = form.data['idade']
            data = form.data['data']
            email = form.data['email']
            form.cleaned_data
            return HttpResponse('Formulário enviado')
        else:
            return render(request, 'home.html', context={
            'form': form
            })