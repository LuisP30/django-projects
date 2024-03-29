from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    if request.session.get('logado'):
        return render(request, 'home.html')
    else:
        return redirect(f'{reverse("usuarios:login")}?status=2')
