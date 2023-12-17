from django.contrib import admin
from .models import Cargos, Pessoa, Pedido
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse

# Na página de administração irá aparecer os pedidos que a pessoa fez na página de cada pessoa
class PedidoInline(admin.TabularInline):
    list_display = ('nome', 'quantidade', 'descricao')
    model = Pedido
    extra = 0 # Para que não fique aparecendo vários campos para adicionar novo pedido

@admin.register(Pessoa)
class PessoaAdmin(DjangoObjectActions, admin.ModelAdmin):
    inlines = [PedidoInline]                                  # Criei uma função chamada get_nome_completo onde retorna nome e sobrenome, especificando ela nessa tupla os nomes dos usuários irão aparecer completos na listagem
    list_display = ('get_image', 'nome', 'email', 'password', 'get_nome_completo') # Mostrando mais informações do usuário na tela de listagem dos usuários
    readonly_fields = ('password', 'cargo') # Campos permitido apenas leitura
    #search_fields = ('nome', 'senha') # Aqui estou permitindo que os usuários sejam pesquisados por nome ou senha na barra de busca
    list_filter = ('cargo',) # Aqui são os campos que poderei filtrar
    list_editable = ('email',) # Aqui poderei alterar o campo email sem precisar entrar na página do usuário especifico

    def mostra_pessoa(self, request, pessoa):
        return HttpResponse(pessoa)

    mostra_pessoa.label = 'mostra pessoa'
    change_actions = ('mostra_pessoa',)

admin.site.register(Cargos)
admin.site.register(Pedido)