from django.db import models


class Cargos(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    sobrenome = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    senha = models.CharField(max_length=50, blank=False, null=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    cargo = models.ManyToManyField(Cargos)

    def __str__(self):
        return self.nome
