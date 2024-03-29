import os
import keyboard

class Calculadora:
    def __init__(self):
        # Constructor: se llama cuando se crea un nuevo objeto
        self.numero1 = 0
        self.numero2 = 0

    def set_numeros(self, num1, num2):
        # Método para establecer los números a operar
        self.numero1 = num1
        self.numero2 = num2

    def solicitar_numeros(self):
        # Método para solicitar los números al usuario
        try:
            self.numero1 = float(input("Ingrese el primer número: "))
            self.numero2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Ingrese números válidos.")

    def limpiar_consola(self):
        # Método para limpiar la consola
        os.system('cls' if os.name == 'nt' else 'clear')

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "No se puede dividir por cero"

# Ciclo principal
while True:
    # Uso de la calculadora
    mi_calculadora = Calculadora()

    # Limpiar la consola
    mi_calculadora.limpiar_consola()

    # Solicitar números al usuario
    mi_calculadora.solicitar_numeros()

    # Operaciones
    resultado_suma = mi_calculadora.sumar()
    resultado_resta = mi_calculadora.restar()
    resultado_multiplicacion = mi_calculadora.multiplicar()
    resultado_division = mi_calculadora.dividir()

    # Mostrar resultados
    print("Suma:", resultado_suma)
    print("Resta:", resultado_resta)
    print("Multiplicación:", resultado_multiplicacion)
    print("División:", resultado_division)

    # Preguntar si desea salir
    print("\nPresiona 'Esc' para salir, o cualquier otra tecla para continuar.")
    if keyboard.read_event().name == 'esc':
        break

