from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    pontos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome
    
    def add_pontos(self):
        self.pontos += 10
    