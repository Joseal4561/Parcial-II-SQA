import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.conversor_unidades import ConversorUnidades

class TestConversorUnidades(unittest.TestCase):
    
    def setUp(self):
        self.conversor = ConversorUnidades()
    
    def test_convertir_longitud(self):
        # 1 metro = 100 centímetros
        self.assertAlmostEqual(self.conversor.convertir_longitud(1, "m", "cm"), 100, places=2)
        # 1 kilómetro = 1000 metros
        self.assertAlmostEqual(self.conversor.convertir_longitud(1, "km", "m"), 1000, places=2)
    
    def test_convertir_peso(self):
        # 1 kilogramo = 1000 gramos
        self.assertAlmostEqual(self.conversor.convertir_peso(1, "kg", "g"), 1000, places=2)
        # 1 libra ≈ 453.592 gramos
        self.assertAlmostEqual(self.conversor.convertir_peso(1, "lb", "g"), 453.592, places=2)
    
    def test_convertir_temperatura(self):
        # 0°C = 32°F
        self.assertAlmostEqual(self.conversor.convertir_temperatura(0, "C", "F"), 32, places=2)
        # 100°C = 212°F
        self.assertAlmostEqual(self.conversor.convertir_temperatura(100, "C", "F"), 212, places=2)
        # 0°C = 273.15°K
        self.assertAlmostEqual(self.conversor.convertir_temperatura(0, "C", "K"), 273.15, places=2)
    
    def test_convertir_volumen(self):
        # 1 litro = 1000 mililitros
        self.assertAlmostEqual(self.conversor.convertir_volumen(1, "l", "ml"), 1000, places=2)
        # 1 galón ≈ 3.78541 litros
        self.assertAlmostEqual(self.conversor.convertir_volumen(1, "gal", "l"), 3.78541, places=2)
    
    def test_unidades_invalidas(self):
        with self.assertRaises(ValueError):
            self.conversor.convertir_longitud(1, "xyz", "m")
        
        with self.assertRaises(ValueError):
            self.conversor.convertir_temperatura(1, "X", "C")

if __name__ == '__main__':
    unittest.main()