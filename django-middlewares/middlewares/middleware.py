from django.http import HttpResponse

def middleware_forbiden(get_response):
    # Código de inicialização do Middleware
    def middleware(request):
        # Aqui vai o código a ser executado antes da view
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        # Interceptando requisição do usuário antes de chegar na view
        if request.META['REMOTE_ADDR'] == '127.0.0.1':
            return HttpResponse('Você está bloqueado', status=403)
        response = get_response(request)
        # Interceptando a resposta da view para o usuário
        print(response)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Aqui vai o código a ser executado depois da view
        
        return response

    return middleware