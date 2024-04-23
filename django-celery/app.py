from tarefas import exibir

x = exibir.delay()
print(x)

# celery -A tarefas worker --loglevel=INFO