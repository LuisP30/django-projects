from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('', lambda request: redirect('/auth/login/')), # Sempre que eu acessar uma URL vazia, serei redirecionado para login
    path('plataforma/', include('plataforma.urls')),
]
