from django.shortcuts import render
from .tasks import minha_tarefa
from django.http import HttpResponse

def home(request):
    minha_tarefa.delay() # Enviando minha tarefa celery para o broker
    return HttpResponse('Página Inicial')
