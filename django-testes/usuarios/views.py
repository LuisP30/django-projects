from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import get_object_or_404

# def home(request):
    # Pegando parâmetro enviado na URL #
    # id = request.GET.get('id')
    # if id == '1':
        # return HttpResponse('Hello')
    # else:
        # return HttpResponse(status=500)
    
def home(request):
    email = request.GET.get('email')
    usuario = get_object_or_404(Usuario, email=email)
    return HttpResponse('Teste')