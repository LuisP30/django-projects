from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pessoa, Historico
# Signals

# Minha função de callback
@receiver(post_save, sender=Pessoa)
def envia_sinal(sender, instance, created, **kwargs):
    # Salvando os dados do usuário em um histórico sempre que ele alterar seus dados
    x = Historico(nome=instance.nome, email=instance.email, telefone=instance.telefone, pessoa=instance)
    x.save()
    print('Histórico cadastrado')

# Outra forma de fazer o post.save:
# post_save.connect(envia_sinal, sender=Pessoa) # Sempre após salvar algo no model Pessoa, a função envia_sinal é chamada