from django import forms
from .models import *

# MODEL FORM
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('nome', 'descricao', 'n_paginas',) # ou '__all__'



# FORM DO DJANGO

# class Cliente(forms.Form):
#     nome = forms.CharField(max_length=20)
#     idade = forms.IntegerField()
#     data = forms.DateField()
#     email = forms.EmailField()

    # def __init__(self, alterar = True, classe = 'form-control', *args, **kwargs): # Eu que criei as variáveis alterar e class
    #     super().__init__(*args, **kwargs)
    #     if alterar:
    #         # Adicionando o atributo classe ao input nome
    #         self.fields['nome'].widget.attrs['class'] = classe
    #         # Adicionando o atributo placeholder ao input nome
    #         self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
    #         # Adicionando o atributo classe ao input idade
    #         self.fields['idade'].widget.attrs['class'] = classe
    #         self.fields['idade'].widget.attrs['placeholder'] = 'Informe a sua idade'
    #         # Adicionando o atributo placeholder ao input idade
    #         self.fields['data'].widget.attrs['class'] = 'form-control'
    #         self.fields['data'].widget.attrs['placeholder'] = 'Defina a data'
    #         self.fields['email'].widget.attrs['class'] = 'form-control'
    #         self.fields['email'].widget.attrs['placeholder'] = 'Seu email'