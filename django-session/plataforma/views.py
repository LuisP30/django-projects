from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url = 'usuarios:login')
def home(request):
    form_cliente = Cliente(alterar=True, classe='teste')
    input_alterar = ('nome', 'idade')
    for i in form_cliente.fields.keys():
        if i in input_alterar:
            try:
                classe_anterior = form_cliente.fields[i].widget.attrs['class']
            except KeyError:
                classe_anterior = ''
            form_cliente.fields[i].widget.attrs['class'] = classe_anterior + ' form-control'
            

    return render(request, 'home.html', context={
        'form': form_cliente
    })