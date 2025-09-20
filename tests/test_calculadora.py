import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_suma(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0.1, 0.2), 0.3)
    
    def test_resta(self):
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(-1, -1), 0)
    
    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
    
    def test_division(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
    
    def test_potencia(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
    
    def test_raiz_cuadrada(self):
        self.assertEqual(self.calc.raiz_cuadrada(9), 3)
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-1)

if __name__ == '__main__':
    unittest.main()