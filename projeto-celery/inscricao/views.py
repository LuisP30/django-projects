from django.shortcuts import render

def inscricao(request):
    return render(request, 'inscricao/inscricao.html')