from interessados import *
from interface import *
from turmas import *

i1 = Interessados('Luis', 'luis@gmail.com')
i2 = Interessados('Henrique', 'henrique@gmail.com')
i3 = Interessados('Pimenta', 'pimenta@gmail.com')

turma_pf = Turmas()
turma_pf.add_interessado(i1)
turma_pf.add_interessado(i2)
turma_pf.add_interessado(i3)
turma_pf.add_turma('Turma 1.0')

print(turma_pf.interessados)