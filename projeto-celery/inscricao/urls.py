from django.urls import path
from . import views

app_name = 'inscricao'

urlpatterns = [
    path('', views.inscricao, name='inscricao')
]
