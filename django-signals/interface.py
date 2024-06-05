# Implementando o padrão de projeto Observer
from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def update_add(self):
        pass

    
