from ninja import Router
from django.http import JsonResponse

pacientes_router = Router()

@pacientes_router.get('/')
def teste(request):
    return JsonResponse({'paciente': 2})