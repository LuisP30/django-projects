from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from .models import Profile
from django.contrib.auth.models import User

# Signal para quando o objeto é salvo no banco
@receiver(post_save, sender=User)
def cria_profile(sender, instance, created, **kwargs):
    if created:
        x = Profile(usuario=instance)
        print('Perfil foi instanciado aqui')
        x.save()
    print('Signal chamado')

# Signal para quando o objeto é instanciado
@receiver(pre_save, sender=Profile)
def profile_instanciado(sender, instance, raw, **kwargs):
    print('Perfil instanciado')

# Signal de delete
@receiver(post_delete, sender=Profile)
def exclui_perfil(sender, instance, using, origin, **kwargs):
    print(origin)
    print(f'Perfil {instance} excluído')