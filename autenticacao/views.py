from django.shortcuts import render
import datetime


def login(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    data = datetime.datetime.now().time()
    return render(request, 'login.html', context={
        'nome': nome,
        'sobrenome': sobrenome,
        'data': data,
    })


def cadastro(request):
    ...
