from abc import ABC, abstractmethod
from .i_component import IComponent

class ICalculadora(IComponent):
    """Interface para la calculadora"""
    
    @abstractmethod
    def sumar(self, a: float, b: float) -> float:
        pass
    
    @abstractmethod
    def restar(self, a: float, b: float) -> float:
        pass
    
    @abstractmethod
    def multiplicar(self, a: float, b: float) -> float:
        pass
    
    @abstractmethod
    def dividir(self, a: float, b: float) -> float:
        pass
    
    @abstractmethod
    def potencia(self, base: float, exponente: float) -> float:
        pass