from abc import ABC, abstractmethod
from typing import List, Dict
from .i_component import IComponent

class IGestorTareas(IComponent):
    """Interface para el gestor de tareas"""
    
    @abstractmethod
    def agregar_tarea(self, descripcion: str, prioridad: str = "media") -> int:
        pass
    
    @abstractmethod
    def completar_tarea(self, id_tarea: int) -> bool:
        pass
    
    @abstractmethod
    def eliminar_tarea(self, id_tarea: int) -> bool:
        pass
    
    @abstractmethod
    def listar_tareas(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def buscar_tareas(self, termino: str) -> List[Dict]:
        pass