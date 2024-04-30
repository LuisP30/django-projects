from celery import Celery
from random import randint

app = Celery(broker='redis://127.0.0.1:6379/0')

@app.task(bind = True, max_retries = 3, default_retry_delay = 2, autoretry_for =(ZeroDivisionError, ValueError)) 
# bind faz com que eu tenha acesso a task. default_retry_delay = Tempo que a atividade deve ser executada novamente em caso de erro
# max_retries = Quantidade de tentativas máximas que ele vai tentar
# autoretry_for recebe uma tupla de erros. Caso dê um erro que está dentro da minha tupla, ele irá tentar novamente
def exibir(self): # Por ter o bind como True, eu consigo utilizar o self
    x = randint(1, 9)
    if x > 7:
        return x
    else:
        raise ValueError('Erro')