from ninja import Router
from django.http import JsonResponse

pacientes_router = Router() 

@pacientes_router.get('/', auth=None) # Definindo o auth como None, esse endpoint fica livre da autenticação global
def teste(request):
    return JsonResponse({'paciente': 2})