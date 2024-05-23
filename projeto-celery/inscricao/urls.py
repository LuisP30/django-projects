from django.urls import path
from . import views

app_name = 'inscricao'

urlpatterns = [
    path('', views.inscricao, name='inscricao'),
    path('email/<path:email>/<path:nome>', views.envia_email, name='envia_email'), # URL que recebe um argumento
]
