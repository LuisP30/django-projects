from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url = 'usuarios:login')
def home(request):
    form_cliente = Cliente()
    return render(request, 'home.html', context={
        'form': form_cliente
    })