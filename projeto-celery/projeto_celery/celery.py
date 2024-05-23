import os
from celery import Celery

# Definindo uma variável de ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_celery.settings') # <-- Nome do meu projeto django

app = Celery('projeto_celery') # As configurações do broker serão feitas no arquivo settings.py do meu projeto django

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debub_task(self):
    print(f'Request: {self.request!r}')