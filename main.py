"""
Menú principal del sistema
Integra todos los componentes del proyecto
"""

import sys
import os

# Agregar el directorio actual al path para importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.calculadora import Calculadora
from src.gestor_tareas import GestorTareas
from src.conversor_unidades import ConversorUnidades

class MenuPrincipal:
    """Menú principal que integra todos los componentes"""
    
    def __init__(self):
        self.componentes = {
            "1": Calculadora(),
            "2": GestorTareas(),
            "3": ConversorUnidades()
        }
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print("SISTEMA INTEGRADO DE HERRAMIENTAS")
        print("Proyecto QA Software - Parcial II")
        print("="*50)
        print("\nComponentes disponibles:")
        
        for key, componente in self.componentes.items():
            print(f"{key}. {componente.get_name()}")
            print(f"   {componente.get_description()}")
        
        print("0. Salir")
        print("-"*50)
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "0":
                print("\n¡Gracias por usar el sistema!")
                print("Desarrollado por: José, Gerbert y Jason")
                break
            elif opcion in self.componentes:
                try:
                    self.componentes[opcion].execute()
                except KeyboardInterrupt:
                    print("\n\nOperación cancelada por el usuario")
                except Exception as e:
                    print(f"\nError inesperado: {e}")
            else:
                print("\nOpción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ejecutar()