from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Estou na página home</h1>')