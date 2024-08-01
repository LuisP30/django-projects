from django.http import HttpResponse

def middleware_forbiden(get_response):
    # Código de inicialização do Middleware
    def middleware(request):
        # Aqui vai o código a ser executado antes da view
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        # Interceptando requisição do usuário antes de chegar na view
        # if request.META['REMOTE_ADDR'] == '127.0.0.1':
        #     return HttpResponse('Você está bloqueado', status=403)
        response = get_response(request)
        # Interceptando a resposta da view para o usuário
        print(response)
        html = '<h1>Fui interceptado</h1>'.encode()
        response.content = html

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Aqui vai o código a ser executado depois da view
        
        return response

    return middleware


# Também é possível com classes:
class MiddlewareForbiden:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Controla request
        response = self.get_response(request)
        # Controla response
        
        return response