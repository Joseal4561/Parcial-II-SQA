import math
from interfaces.i_calculadora import ICalculadora


class Calculadora(ICalculadora):
    """Calculadora científica con operaciones básicas y avanzadas"""
    
    def get_name(self) -> str:
        return "Calculadora Científica"
    
    def get_description(self) -> str:
        return "Calculadora con operaciones matemáticas básicas y científicas"
    
    def sumar(self, a: float, b: float) -> float:
        return a + b
    
    def restar(self, a: float, b: float) -> float:
        return a - b
    
    def multiplicar(self, a: float, b: float) -> float:
        return a * b
    
    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def potencia(self, base: float, exponente: float) -> float:
        return base ** exponente
    
    def raiz_cuadrada(self, numero: float) -> float:
        if numero < 0:
            raise ValueError("No se puede calcular raíz cuadrada de número negativo")
        return math.sqrt(numero)
    
    def seno(self, angulo: float) -> float:
        return math.sin(math.radians(angulo))
    
    def coseno(self, angulo: float) -> float:
        return math.cos(math.radians(angulo))
    
    def execute(self) -> None:
        print(f"\n=== {self.get_name()} ===")
        print(self.get_description())
        
        while True:
            print("\nOperaciones disponibles:")
            print("1. Suma")
            print("2. Resta") 
            print("3. Multiplicación")
            print("4. División")
            print("5. Potencia")
            print("6. Raíz cuadrada")
            print("7. Seno")
            print("8. Coseno")
            print("0. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion in ["1", "2", "3", "4", "5"]:
                try:
                    a = float(input("Ingrese el primer número: "))
                    b = float(input("Ingrese el segundo número: "))
                    
                    if opcion == "1":
                        resultado = self.sumar(a, b)
                    elif opcion == "2":
                        resultado = self.restar(a, b)
                    elif opcion == "3":
                        resultado = self.multiplicar(a, b)
                    elif opcion == "4":
                        resultado = self.dividir(a, b)
                    elif opcion == "5":
                        resultado = self.potencia(a, b)
                    
                    print(f"Resultado: {resultado}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif opcion in ["6", "7", "8"]:
                try:
                    numero = float(input("Ingrese el número: "))
                    
                    if opcion == "6":
                        resultado = self.raiz_cuadrada(numero)
                    elif opcion == "7":
                        resultado = self.seno(numero)
                    elif opcion == "8":
                        resultado = self.coseno(numero)
                    
                    print(f"Resultado: {resultado}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Opción no válida")