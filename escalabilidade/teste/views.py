from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Usuario

@cache_page(60) # 1 minuto
def teste(request):
    usuarios = Usuario.objects.all()
    return render(request, 'teste.html', context={
        'usuarios': usuarios,
    })