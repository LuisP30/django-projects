from time import sleep
from datetime import datetime
from celery import shared_task
from .models import DataAtual

# Após um período de tempo a data do meu banco de dados será atualizada
@shared_task(bind=True)
def atualiza_banco(self):
    data_atual = DataAtual.objects.all().first()
    data_atual.data_atual = datetime.now()
    data_atual.save()
    return 'Done'