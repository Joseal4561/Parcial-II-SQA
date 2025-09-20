from abc import ABC, abstractmethod

class IComponent(ABC):
    """Interface base para todos los componentes"""
    
    @abstractmethod
    def get_name(self) -> str:
        """Retorna el nombre del componente"""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Retorna la descripción del componente"""
        pass
    
    @abstractmethod
    def execute(self) -> None:
        """Ejecuta la funcionalidad principal"""
        pass