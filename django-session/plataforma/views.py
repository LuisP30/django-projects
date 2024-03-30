from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages

def home(request):
    try:
        if request.session['logado']:
            return render(request, 'home.html')
    except KeyError:
        messages.add_message(request, constants.INFO, 'Faça login antes de acessar o sistema')
        return redirect("usuarios:login")
