# interfaces/__init__.py
"""
Módulo de interfaces para el proyecto QA Software
"""

from .i_component import IComponent
from .i_calculadora import ICalculadora
from .i_gestor_tareas import IGestorTareas
from .i_conversor import IConversor

__all__ = ['IComponent', 'ICalculadora', 'IGestorTareas', 'IConversor']