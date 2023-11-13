from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('perfil/<int:id>/', views.perfil, name='perfil'),
    path('edit/<int:id>/', views.editar_pessoa, name='edit'),
    path('delete/<int:id>/', views.excluir_pessoa, name='delete'),

]
