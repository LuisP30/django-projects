from django.contrib import admin
from .models import Cargos, Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'password') # Mostrando mais informações do usuário na tela de listagem dos usuários
    readonly_fields = ('password', 'cargo') # Campos permitido apenas leitura
    search_fields = ('nome', 'senha') # Aqui estou permitindo que os usuários sejam pesquisados por nome ou senha na barra de busca
    list_filter = ('cargo',) # Aqui são os campos que poderei filtrar
    list_editable = ('email',) # Aqui poderei alterar o campo email sem precisar entrar na página do usuário especifico

admin.site.register(Cargos)
