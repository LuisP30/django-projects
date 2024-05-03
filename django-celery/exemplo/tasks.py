from time import sleep
from celery import shared_task

@shared_task # Com esse decorator estou informando que essa função é uma task do celery
def minha_tarefa():
    sleep(10)
    return 'teste'