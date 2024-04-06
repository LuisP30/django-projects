from django import forms

class Cliente(forms.Form):
    nome = forms.CharField(max_length=20)
    idade = forms.IntegerField()