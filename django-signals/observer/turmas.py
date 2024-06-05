# Importa a classe Interessados do módulo interessados
from interessados import Interessados

# Define a classe Turmas, responsável por gerenciar turmas e interessados
class Turmas:
    # Inicializa a classe com listas vazias para turma e interessados
    def __init__(self):
        self.turma = []
        self.interessados = []

    # Adiciona um interessado à lista de interessados
    def add_interessado(self, interessado: Interessados):
        self.interessados.append(interessado)

    # Adiciona uma nova turma à lista de turmas
    def add_turma(self, nova_turma):
        self.turma.append(nova_turma)

        # Notifica todos os interessados sobre a nova turma
        for interessado in self.interessados:
            interessado.update_add()
