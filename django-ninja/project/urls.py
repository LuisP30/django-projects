from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls), # Versão da API
    # api.urls estão todas as urls que criei com add_router()
    # api.py no project é onde está a instância de NinjaAPI
    # Essa URL aponta para todas as rotas da minha API
] 
