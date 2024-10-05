from ninja import NinjaAPI
from alimentos.api.api import alimentos_router # Nesse app eu criei uma pasta chamada api
from pacientes.api import pacientes_router

api = NinjaAPI()

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)