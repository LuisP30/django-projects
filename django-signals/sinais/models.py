from django.db import models
from django.db.models.signals import post_save

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome


def envia_sinal(sender, instance, created, **kwargs):
    print('Fui chamada')

# Aqui passo qual será o sinal enviado. sender é a classe que está sendo observada
post_save.connect(envia_sinal, sender=Pessoa) # Sempre após salvar algo no model Pessoa, a função envia_sinal é chamada