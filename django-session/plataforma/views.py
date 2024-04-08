from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url = 'usuarios:login')
def home(request):
    if request.method == 'GET':
        form = LivroForm()
        return render(request, 'home.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            form = LivroForm()
            messages.add_message(request, constants.SUCCESS, 'Livro salvo com sucesso!')
            return redirect('plataforma:home')
        else:
            return render(request, 'home.html', context={
            'form': form
        })