from interessados import Interessados

class Turmas:
    def __init__(self):
        self.turma = []
        self.interessados = []

    def add_interessado(self, interessado: Interessados):
        self.interessados.append(interessado)

    def add_turma(self, nova_turma):
        self.turma.append(nova_turma)

        for interessado in self.interessados:
            interessado.update_add()