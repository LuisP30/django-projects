from django.db import models
from django.db.models import F

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()

    class Meta:
        indexes = [
            
            models.Index(fields=['nome'], name='nome_usuario'),
            models.Index(fields=['sobrenome'], name='sobrenome_usuario'),
            
            # Abaixo estou criando um indice que otimiza a busca pelo nome completo do usuário
            models.Index(fields=['nome', 'sobrenome'], name='nome_completo_usuario'),
            
            # F permite que sejam feitas operações com as próprias colunas do Model
            models.Index(F('nota1') + F('nota2'), name='soma_nota')
        ]

    def __str__(self):
        return self.nome