from abc import ABC, abstractmethod
from .i_component import IComponent

class IConversor(IComponent):
    """Interface para el conversor de unidades"""
    
    @abstractmethod
    def convertir_longitud(self, valor: float, de: str, a: str) -> float:
        pass
    
    @abstractmethod
    def convertir_peso(self, valor: float, de: str, a: str) -> float:
        pass
    
    @abstractmethod
    def convertir_temperatura(self, valor: float, de: str, a: str) -> float:
        pass
    
    @abstractmethod
    def convertir_volumen(self, valor: float, de: str, a: str) -> float:
        pass