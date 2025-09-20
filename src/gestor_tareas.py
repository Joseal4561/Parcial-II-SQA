import json
import os
from datetime import datetime
from typing import List, Dict
from interfaces.i_gestor_tareas import IGestorTareas

class GestorTareas(IGestorTareas):
    """Gestor de tareas con persistencia en archivo JSON"""
    
    def __init__(self, archivo: str = "tareas.json"):
        self.archivo = archivo
        self.tareas = self._cargar_tareas()
        self._proximo_id = max([t["id"] for t in self.tareas], default=0) + 1
    
    def get_name(self) -> str:
        return "Gestor de Tareas"
    
    def get_description(self) -> str:
        return "Sistema de gestión de tareas con prioridades y persistencia"
    
    def _cargar_tareas(self) -> List[Dict]:
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _guardar_tareas(self) -> None:
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.tareas, f, indent=2, ensure_ascii=False)
    
    def agregar_tarea(self, descripcion: str, prioridad: str = "media") -> int:
        if prioridad not in ["alta", "media", "baja"]:
            raise ValueError("Prioridad debe ser: alta, media o baja")
        
        tarea = {
            "id": self._proximo_id,
            "descripcion": descripcion,
            "prioridad": prioridad,
            "completada": False,
            "fecha_creacion": datetime.now().isoformat()
        }
        
        self.tareas.append(tarea)
        self._guardar_tareas()
        self._proximo_id += 1
        return tarea["id"]
    
    def completar_tarea(self, id_tarea: int) -> bool:
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                tarea["fecha_completada"] = datetime.now().isoformat()
                self._guardar_tareas()
                return True
        return False
    
    def eliminar_tarea(self, id_tarea: int) -> bool:
        for i, tarea in enumerate(self.tareas):
            if tarea["id"] == id_tarea:
                del self.tareas[i]
                self._guardar_tareas()
                return True
        return False
    
    def listar_tareas(self) -> List[Dict]:
        return self.tareas.copy()
    
    def buscar_tareas(self, termino: str) -> List[Dict]:
        termino = termino.lower()
        return [t for t in self.tareas if termino in t["descripcion"].lower()]
    
    def execute(self) -> None:
        print(f"\n=== {self.get_name()} ===")
        print(self.get_description())
        
        while True:
            print("\nOpciones disponibles:")
            print("1. Agregar tarea")
            print("2. Listar tareas")
            print("3. Completar tarea")
            print("4. Eliminar tarea")
            print("5. Buscar tareas")
            print("0. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                descripcion = input("Descripción de la tarea: ")
                prioridad = input("Prioridad (alta/media/baja) [media]: ").lower() or "media"
                try:
                    id_tarea = self.agregar_tarea(descripcion, prioridad)
                    print(f"Tarea agregada con ID: {id_tarea}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif opcion == "2":
                tareas = self.listar_tareas()
                if not tareas:
                    print("No hay tareas registradas")
                else:
                    print("\nTareas:")
                    for tarea in tareas:
                        estado = "✓" if tarea["completada"] else "○"
                        print(f"{estado} [{tarea['id']}] {tarea['descripcion']} ({tarea['prioridad']})")
            
            elif opcion == "3":
                try:
                    id_tarea = int(input("ID de la tarea a completar: "))
                    if self.completar_tarea(id_tarea):
                        print("Tarea completada")
                    else:
                        print("Tarea no encontrada")
                except ValueError:
                    print("ID inválido")
            
            elif opcion == "4":
                try:
                    id_tarea = int(input("ID de la tarea a eliminar: "))
                    if self.eliminar_tarea(id_tarea):
                        print("Tarea eliminada")
                    else:
                        print("Tarea no encontrada")
                except ValueError:
                    print("ID inválido")
            
            elif opcion == "5":
                termino = input("Término de búsqueda: ")
                resultados = self.buscar_tareas(termino)
                if not resultados:
                    print("No se encontraron tareas")
                else:
                    print("\nResultados:")
                    for tarea in resultados:
                        estado = "✓" if tarea["completada"] else "○"
                        print(f"{estado} [{tarea['id']}] {tarea['descripcion']} ({tarea['prioridad']})")
            else:
                print("Opción no válida")