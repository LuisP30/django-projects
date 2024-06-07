from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome


class Historico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)

