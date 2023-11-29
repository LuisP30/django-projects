from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'autenticacao'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('perfil/', views.perfil, name='perfil'),
    path('edit/<int:id>/', views.editar_pessoa, name='edit'),
    path('delete/<int:id>/', views.excluir_pessoa, name='delete'),

]
