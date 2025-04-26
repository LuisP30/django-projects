from typing import Any, Dict
from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.types import DictStrAny
from alimentos.api.api import alimentos_router # Nesse app eu criei uma pasta chamada api
from pacientes.api import pacientes_router
from ninja.parser import Parser
import yaml
from ninja.security import HttpBearer, HttpBasicAuth
from django.contrib import auth

# Caso os dados recebidos no corpo da requisição sejam yaml. (Geralmente usado em sistemas legados)
# class YamlParser(Parser):
#     def parse_body(self, request: HttpRequest) -> Dict[str, Any]:
#         return yaml.safe_load(request.body)
    
# api = NinjaAPI(parser=YamlParser()) # É necessário alterar o parser do NinjaAPI


# AUTENTICAÇÃO
# Nesse caso a autenticação ficará de forma global
# class MyAuth(HttpBearer):
#     def authenticate(self, request: HttpRequest, token: str):
#         if token == '1234':
#             return token

# Autenticação Basic Auth
class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        if user:
            return user.id
        # Os valores são recebidos de maneira codificadas (base64) e são decodificadas no back-end


api = NinjaAPI(auth=BasicAuth()) # Especificando em auth qual class será utilizada para autenticação: NinjaAPI(auth=MyAuth())
api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)

"""
Nesse projeto foi configurado dois tipos de autenticação. Em alguns exemplos foi citado a autenticação de HttpBearer
e em outros foi citado o HttpBasicAuth. HttpBasicAuth foi o método utilizado como o principal.
"""