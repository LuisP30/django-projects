from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Sala
from django.db.models import Q
from django.http import HttpResponse

def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nomeSala')
        senha = request.POST.get('senhaSala')
        
        sala = Sala.objects.filter(Q(nome=nome) & Q(senha = senha)).first() # É como se eu utilizasse dois filter (AND)
        
        if sala:
            return redirect(reverse('chat', args=(sala.nome,)))
        else:
            return HttpResponse('Nome ou senha inexistente')
        
def chat(request, nome):
    return render(request, 'chat.html', {
        'nome': nome
    })