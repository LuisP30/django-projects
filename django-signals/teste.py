# Importa tudo dos módulos interessados, interface e turmas
from interessados import *
from interface import *
from turmas import *

# Cria instâncias da classe Interessados
i1 = Interessados('Luis', 'luis@gmail.com')
i2 = Interessados('Henrique', 'henrique@gmail.com')
i3 = Interessados('Pimenta', 'pimenta@gmail.com')

# Cria uma instância da classe Turmas
turma_pf = Turmas()

# Adiciona os interessados à turma_pf
turma_pf.add_interessado(i1)
turma_pf.add_interessado(i2)
turma_pf.add_interessado(i3)

# Adiciona uma nova turma e notifica os interessados
turma_pf.add_turma('Turma 1.0')

# Imprime a lista de interessados da turma_pf
print(turma_pf.interessados)


"""
interface.py: Define a interface (classe abstrata Observador) que contém o método 
update_add que todas as classes observadoras devem implementar.

interessados.py: Implementa a classe Interessados, que herda de Observador e define 
o método update_add para notificar o interessado quando uma nova turma é adicionada.

turmas.py: Define a classe Turmas, que mantém uma lista de turmas e de interessados. 
Ao adicionar uma nova turma, todos os interessados são notificados 
através do método update_add.

teste.py: Testa a implementação criando instâncias de Interessados e Turmas, 
adicionando os interessados à turma e depois adicionando uma nova turma, 
desencadeando notificações para todos os interessados.
"""