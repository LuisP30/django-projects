from . import models
from django.contrib.auth.forms import UserCreationForm


class PessoaForm(UserCreationForm):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'sobrenome', 'email', 'password1', 'password2']