from django.db import models
from django.db.models.fields import *
from django.contrib.auth.models import User

class EnderecoUsuario(models.Model):
    rua = CharField(max_length = 100, blank = True, null = True)
    numero = CharField(max_length = 100, blank = True, null = True)
    cep = CharField(max_length = 8, blank = True, null = True)
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.usuario.username
    