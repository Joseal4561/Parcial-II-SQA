import unittest
import os
import tempfile
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    
    def setUp(self):
        # Usar archivo temporal para tests
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        self.gestor = GestorTareas(self.temp_file.name)
    
    def tearDown(self):
        # Limpiar archivo temporal
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_agregar_tarea(self):
        id_tarea = self.gestor.agregar_tarea("Test tarea", "alta")
        self.assertIsInstance(id_tarea, int)
        self.assertTrue(id_tarea > 0)
    
    def test_agregar_tarea_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Test", "invalida")
    
    def test_completar_tarea(self):
        id_tarea = self.gestor.agregar_tarea("Test tarea")
        self.assertTrue(self.gestor.completar_tarea(id_tarea))
        self.assertFalse(self.gestor.completar_tarea(999))  # ID inexistente
    
    def test_eliminar_tarea(self):
        id_tarea = self.gestor.agregar_tarea("Test tarea")
        self.assertTrue(self.gestor.eliminar_tarea(id_tarea))
        self.assertFalse(self.gestor.eliminar_tarea(id_tarea))  # Ya eliminada
    
    def test_listar_tareas(self):
        inicial = len(self.gestor.listar_tareas())
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        self.assertEqual(len(self.gestor.listar_tareas()), inicial + 2)
    
    def test_buscar_tareas(self):
        self.gestor.agregar_tarea("Comprar leche")
        self.gestor.agregar_tarea("Estudiar Python")
        resultados = self.gestor.buscar_tareas("comprar")
        self.assertEqual(len(resultados), 1)
        self.assertIn("leche", resultados[0]["descripcion"].lower())

if __name__ == '__main__':
    unittest.main()