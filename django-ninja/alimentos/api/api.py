from ninja import Router
from django.http import HttpRequest, HttpResponse
from typing import List, Dict
from ninja import Schema
from .schemas import Alimento
from ..models import Alimento as ModelAlimento
from django.shortcuts import get_object_or_404
from ninja.security import HttpBearer
from django.contrib.auth.models import User

alimentos_router = Router()


# AUTENTICAÇÃO
# # Nesse caso a autenticação poderá ser utilizada apenas nessa parte da minha API
# class MyAuth(HttpBearer):
#     def authenticate(self, request: HttpRequest, token: str):
#         if token == '1234':
#             return token
# Então é só passar a instância de MyAuth() em algum endpoint (parâmetro auth de algum decorator)

# alimentos = [
#     {"Nome": "Banana", "Quantidade": 5, "id": 1},
#     {"Nome": "Carne", "Quantidade": 15, "id": 2},
#     {"Nome": "Maçã", "Quantidade": 2, "id": 3},
# ]

# alimento_id é um parâmetro passado na URL. em response especifico o tipo da resposta dessa URL
# @alimentos_router.get('/{int:alimento_id}', response=List[Dict]) 
# (especifiquei o tipo de dado com "int" acima. Essa sintaxe é do Django Ninja)
# def get_alimento(request, alimento_id: int) -> List[Dict] : # type hints do python (int) 
    # Especifiquei o tipo de dado que recebo e retorno. No caso recebo o int e retorno o List[Dict]
    # Abaixo estou filtrando o objeto na lista (alimentos) de acordo com o id recebido como parâmetro na url da requisição
    # alimento = list(filter(lambda x: x["id"] == alimento_id, alimentos)) # Passo como último parâmetro de onde eu quero filtrar
    # return alimento
    
# EXEMPLO RECEBENDO DOIS PARÂMETROS
# @alimentos_router.get('/{int:alimento_id}/{int:categoria_id}/', response=Dict)
# def get_alimento(request, alimento_id: int, categoria_id: int):
#     return JsonResponse({'alimento_id': alimento_id, 'categoria_id': categoria_id})

# @alimentos_router.get('/{int:alimento_id}')
# # Recebendo parâmetros de consulta na URL. preco_min tem que ser do tipo float e o seu valor padrão é 10
# def get_alimento(request, alimento_id: int, preco_min: float = 10): 
#     return {'alimento_id': alimento_id, 'preco_min': preco_min}


# Utilizando POSTMAN e Schemas

# A requisição será post
# @alimentos_router.post('/{int:alimento_id}')
# def get_alimento(request, alimento: Alimento): # <- Recebendo dados no corpo da requisição. O parâmetro alimento é do tipo Alimento
#     print(alimento)
#     return {'alimento_id': 1}


# Trabalhando com Models // Se eu quiser que precise de autenticação apenas em um endpoint, passo o parâmetro auth no decorator abaixo
@alimentos_router.get('/{int:alimento_id}/', response=Alimento) # Definindo que a resposta será do tipo Alimento (Schema)
# Recebendo a requisição e a resposta como parâmetro e informado o tipo de cada uma delas
def get_alimento(request: HttpRequest, response: HttpResponse , alimento_id: int):
    # Adicionando um cookie
    response.set_cookie('teste_aula', '124')
    alimento = ModelAlimento.objects.get(id=alimento_id)
    # User.objects.get(id=request.user)
    print(alimento)
    print(request.auth)
    return alimento

# Criando um objeto com post
@alimentos_router.post('/', response=Alimento)
def create_alimento(request, alimento: Alimento):
    x = ModelAlimento.objects.create(titulo=alimento.titulo, quantidade=alimento.quantidade)
    x.save()
    return x