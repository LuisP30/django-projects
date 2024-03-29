from django.urls import include, path
from .views import *

app_name = 'plataforma'

urlpatterns = [
    path('home/', home, name='home')
]
