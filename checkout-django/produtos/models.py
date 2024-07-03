from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

    def exibe_preco(self):
        return "{:.2f}".format(self.preco)
    
class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    nome = models.CharField(max_length=60)
    status = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)