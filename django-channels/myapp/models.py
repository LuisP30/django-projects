from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=30)
    senha = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome
    