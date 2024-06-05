# Importa classes abstratas e métodos abstratos do módulo abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Define a classe Observador como uma classe abstrata, usando ABC como base
class Observador(ABC):
    # Declara um método abstrato update_add que deve ser implementado por subclasses
    @abstractmethod
    def update_add(self):
        pass
