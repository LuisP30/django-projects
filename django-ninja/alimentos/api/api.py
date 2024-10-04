from ninja import NinjaAPI # É responsável por criar as urls dentro do projeto
from django.http import JsonResponse

api = NinjaAPI()

@api.get('')
def teste(request):
    return JsonResponse({'teste': 1})