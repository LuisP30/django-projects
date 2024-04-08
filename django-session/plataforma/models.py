from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    n_paginas = models.IntegerField()

    def __str__(self) -> str:
        return self.name
