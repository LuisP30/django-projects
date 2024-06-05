from interface import Observador

class Interessados(Observador):

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def update_add(self):
        print(f'Estou informando o {self.nome} no email {self.email} que foi aberta uma nova turma da Python Full')

    def __repr__(self):
        return self.nome