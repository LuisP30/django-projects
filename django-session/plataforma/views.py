from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'usuarios:login')
def home(request):
    messages.add_message(request, constants.INFO, 'Olá seja bem vindo!')
    return render(request, 'home.html')