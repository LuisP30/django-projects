from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import get_object_or_404, render
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.messages import get_messages


def home(request):
    email = request.GET.get('email')
    if '@gmail' not in email:
        messages.add_message(request, constants.ERROR, 'Informe um email do G-mail')
        return render(request, 'home.html')
    
    usuario = get_object_or_404(Usuario, email=email)

    if request.GET.get('cond') == '1':
        return render(request, 'home.html')
    else:
        return render(request, 'logar.html')