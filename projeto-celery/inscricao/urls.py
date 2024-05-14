from django.urls import path
from . import views

app_name = 'inscricao'

urlpatterns = [
    path('', views.inscricao, name='inscricao'),
    path('email/<path:email>', views.envia_email, name='envia_email'),
    path('certificado/', views.certificado, name='certificado'),
]
