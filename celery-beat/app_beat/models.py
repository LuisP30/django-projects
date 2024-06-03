from django.db import models

class DataAtual(models.Model):
    data_atual = models.DateTimeField()

    def __str__(self):
        return str(self.data_atual)