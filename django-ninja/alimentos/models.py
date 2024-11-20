from django.db import models

class Alimento(models.Model):
    titulo = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    
    def __str__(self) -> str:
        return self.titulo