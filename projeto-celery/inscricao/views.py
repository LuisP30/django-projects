from django.shortcuts import render, redirect
from django.urls import reverse
from .task import envia_email_com_anexo
from . import models

def inscricao(request):
    if request.POST:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        pessoa = models.Pessoa(nome=nome, email=email)
        pessoa.save()
        return redirect('inscricao:envia_email', email=email, nome=nome) # Atenção a maneira que enviei o email como argumento!
    return render(request, 'inscricao/inscricao.html')
 
def envia_email(request, email, nome):
    envia_email_com_anexo.delay(email, nome)
    return redirect('inscricao:inscricao')
