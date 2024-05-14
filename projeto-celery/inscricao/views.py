from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from . import models

def inscricao(request):
    if request.POST:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        pessoa = models.Pessoa(nome=nome, email=email)
        pessoa.save()
        return redirect('inscricao:envia_email', email=email) # Atenção a maneira que enviei o email como argumento!
    return render(request, 'inscricao/inscricao.html')
 
def envia_email(request, email):
    send_mail('Assunto', 'Essa é a minha mensagem', 'pimenta.lh2@gmail.com', [email])
    return redirect('inscricao:certificado')

def certificado(request):
    return render(request, 'inscricao/certificado.html')