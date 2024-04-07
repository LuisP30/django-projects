from django import forms

class Cliente(forms.Form):
    nome = forms.CharField(max_length=20)
    idade = forms.IntegerField()

    def __init__(self, alterar = None, classe = None, *args, **kwargs): # Eu que criei as variáveis alterar e class
        super().__init__(*args, **kwargs)
        if alterar:
            # Adicionando o atributo classe ao input nome
            self.fields['nome'].widget.attrs['class'] = classe
            # Adicionando o atributo placeholder ao input nome
            self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
            # Adicionando o atributo classe ao input idade
            self.fields['idade'].widget.attrs['class'] = classe
            # Adicionando o atributo placeholder ao input idade
            self.fields['idade'].widget.attrs['placeholder'] = 'Sua idade'