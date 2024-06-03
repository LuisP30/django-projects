import os
from celery import Celery
from celery.schedules import crontab
# ESTE ARQUIVO POSSUI CONFIGURAÇÕES ADICIONAIS PARA O CELERY BEAT
# Definindo uma variável de ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_beat.settings') # <-- Nome do meu projeto django

app = Celery('celery_beat') # As configurações do broker serão feitas no arquivo settings.py do meu projeto django
app.conf.enable_utc = False # new!
app.conf.update(timezone = 'America/Sao_Paulo') # new!
app.config_from_object('django.conf.settings', namespace='CELERY')

# CELERY BEAT CONFIG
app.conf.beat_schedule = {
    'atualiza-banco-todo-dia-00:00': {
        'task': 'app_beat.task.atualiza_banco', # Informo onde a task está
        'schedule': crontab()
    }
} # Neste dicionário vou nomear as tarefas que serão executadas (dou o nome que quiser)

app.autodiscover_tasks()

@app.task(bind=True)
def debub_task(self):
    print(f'Request: {self.request!r}')