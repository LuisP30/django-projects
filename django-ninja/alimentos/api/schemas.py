from typing import List, Dict
from ninja import Schema, ModelSchema
from ninja.orm import ModelSchema as TesteSchema
from ..models import Alimento as ModelAlimento # Criando schemas a partir de models

# class Alimento(Schema): # Coloco aqui o que quero receber no corpo da minha requisição
#     titulo: str
#     quantidade: int
#     variedades: List[str] # Variedades será uma lista de strings (se eu passar um inteiro ele será convertido para string)

# Dessa maneira, esse schema tem todos os campos que o model tem
class Alimento(TesteSchema):
    # Definindo um novo campo para o meu Schema abaixo. Campo do tipo Lista de inteiros com valor padrão Lista vazia
    novo_campo: List[int] = []
    class Config(Schema.Config): # Herdando de Schema.Config para alterar algumas configurações (Inicialmente não herdava nada)
        model = ModelAlimento
        # Definindo abaixo quais campos tem no model que quero manter no Schema
        model_fields = ["titulo", "quantidade", "id"]
        # model_exclude = campos que quero excluir
        # CAMPOS HERDADOS DE SCHEMA.CONFIG
        str_to_lower = True
        str_strip_whitespace = True