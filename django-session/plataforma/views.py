from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

def home(request):
    if request.session['logado']:
        return HttpResponse('Você está no sistema')
    else:
        return redirect(f'{reverse("usuarios:login")}?status=2')
