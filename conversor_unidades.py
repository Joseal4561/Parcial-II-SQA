
from interfaces.i_conversor import IConversor

class ConversorUnidades(IConversor):
    """Conversor de unidades para longitud, peso, temperatura y volumen"""
    
    def __init__(self):
        # Factores de conversión a unidad base (metros, kilogramos, litros)
        self.longitud_factores = {
            "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
            "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34
        }
        
        self.peso_factores = {
            "mg": 0.000001, "g": 0.001, "kg": 1.0, "t": 1000.0,
            "oz": 0.0283495, "lb": 0.453592
        }
        
        self.volumen_factores = {
            "ml": 0.001, "l": 1.0, "m3": 1000.0,
            "fl_oz": 0.0295735, "cup": 0.236588, "pt": 0.473176,
            "qt": 0.946353, "gal": 3.78541
        }
    
    def get_name(self) -> str:
        return "Conversor de Unidades"
    
    def get_description(self) -> str:
        return "Conversor de unidades de longitud, peso, temperatura y volumen"
    
    def convertir_longitud(self, valor: float, de: str, a: str) -> float:
        if de not in self.longitud_factores or a not in self.longitud_factores:
            raise ValueError("Unidad de longitud no soportada")
        
        # Convertir a metros, luego a la unidad destino
        metros = valor * self.longitud_factores[de]
        resultado = metros / self.longitud_factores[a]
        return resultado
    
    def convertir_peso(self, valor: float, de: str, a: str) -> float:
        if de not in self.peso_factores or a not in self.peso_factores:
            raise ValueError("Unidad de peso no soportada")
        
        # Convertir a kilogramos, luego a la unidad destino
        kilogramos = valor * self.peso_factores[de]
        resultado = kilogramos / self.peso_factores[a]
        return resultado
    
    def convertir_temperatura(self, valor: float, de: str, a: str) -> float:
        # Convertir a Celsius primero
        if de == "F":
            celsius = (valor - 32) * 5/9
        elif de == "K":
            celsius = valor - 273.15
        elif de == "C":
            celsius = valor
        else:
            raise ValueError("Unidad de temperatura no soportada (use C, F, K)")
        
        # Convertir de Celsius a la unidad destino
        if a == "F":
            return celsius * 9/5 + 32
        elif a == "K":
            return celsius + 273.15
        elif a == "C":
            return celsius
        else:
            raise ValueError("Unidad de temperatura no soportada (use C, F, K)")
    
    def convertir_volumen(self, valor: float, de: str, a: str) -> float:
        if de not in self.volumen_factores or a not in self.volumen_factores:
            raise ValueError("Unidad de volumen no soportada")
        
        # Convertir a litros, luego a la unidad destino
        litros = valor * self.volumen_factores[de]
        resultado = litros / self.volumen_factores[a]
        return resultado
    
    def execute(self) -> None:
        print(f"\n=== {self.get_name()} ===")
        print(self.get_description())
        
        while True:
            print("\nTipos de conversión:")
            print("1. Longitud")
            print("2. Peso")
            print("3. Temperatura")
            print("4. Volumen")
            print("0. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                self._convertir_longitud_menu()
            elif opcion == "2":
                self._convertir_peso_menu()
            elif opcion == "3":
                self._convertir_temperatura_menu()
            elif opcion == "4":
                self._convertir_volumen_menu()
            else:
                print("Opción no válida")
    
    def _convertir_longitud_menu(self):
        print("\nUnidades disponibles: mm, cm, m, km, in, ft, yd, mi")
        try:
            valor = float(input("Valor a convertir: "))
            de = input("Desde (unidad): ").lower()
            a = input("Hacia (unidad): ").lower()
            resultado = self.convertir_longitud(valor, de, a)
            print(f"{valor} {de} = {resultado:.6f} {a}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _convertir_peso_menu(self):
        print("\nUnidades disponibles: mg, g, kg, t, oz, lb")
        try:
            valor = float(input("Valor a convertir: "))
            de = input("Desde (unidad): ").lower()
            a = input("Hacia (unidad): ").lower()
            resultado = self.convertir_peso(valor, de, a)
            print(f"{valor} {de} = {resultado:.6f} {a}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _convertir_temperatura_menu(self):
        print("\nUnidades disponibles: C (Celsius), F (Fahrenheit), K (Kelvin)")
        try:
            valor = float(input("Valor a convertir: "))
            de = input("Desde (unidad): ").upper()
            a = input("Hacia (unidad): ").upper()
            resultado = self.convertir_temperatura(valor, de, a)
            print(f"{valor}°{de} = {resultado:.2f}°{a}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _convertir_volumen_menu(self):
        print("\nUnidades disponibles: ml, l, m3, fl_oz, cup, pt, qt, gal")
        try:
            valor = float(input("Valor a convertir: "))
            de = input("Desde (unidad): ").lower()
            a = input("Hacia (unidad): ").lower()
            resultado = self.convertir_volumen(valor, de, a)
            print(f"{valor} {de} = {resultado:.6f} {a}")
        except ValueError as e:
            print(f"Error: {e}")
