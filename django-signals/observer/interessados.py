# Importa a classe Observador do módulo interface
from interface import Observador

# Define a classe Interessados, que herda de Observador
class Interessados(Observador):
    
    # Inicializa a classe com os atributos nome e email
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    # Implementa o método abstrato update_add, que imprime uma mensagem de notificação
    def update_add(self):
        print(f'Estou informando o {self.nome} no email {self.email} que foi aberta uma nova turma da Python Full')

    # Define uma representação string da instância, retornando o nome do interessado
    def __repr__(self):
        return self.nome
