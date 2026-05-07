
from abc import ABC, abstractmethod

class EntidadSistema(ABC):
    """Clase base para todas las entidades del sistema."""
    pass

class Servicio(EntidadSistema):
    """Clase abstracta para servicios ofrecidos."""
    
    @abstractmethod
    def calcular_costo(self) -> float:
        pass
    
    @abstractmethod
    def detallar(self) -> str:
        pass