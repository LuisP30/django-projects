from ninja import Router
from django.http import JsonResponse

alimentos_router = Router()

@alimentos_router.get('/{int:alimento_id}') # alimento_id é um parâmetro passado na URL.
# (especifiquei o tipo de dado com "int" acima. Essa sintaxe é do Django Ninja)
def get_alimento(request, alimento_id: int): # type hints do python (int)
    return JsonResponse({'id': alimento_id})