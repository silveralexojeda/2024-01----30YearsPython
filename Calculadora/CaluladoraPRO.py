#HDPerraEstoQuieres-EstoVasAtener
"""
1) Crea una calculadora que:
•sume, reste, multiplique y divida
•maneje los errores y valide los datos ingresados
•tenga interfaz en la terminal, no visual
"""

"""
La Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en 
el concepto de "objetos". Los objetos son instancias de clases, que son plantillas que definen 
la estructura y el comportamiento de los objetos. Python es un lenguaje de programación que soporta 
la POO de manera nativa.

A continuación, te proporcionaré un ejemplo básico de un script de calculadora utilizando 
la programación orientada a objetos en Python:
"""

class Calculadora:
    def __init__(self):
        # Constructor: se llama cuando se crea un nuevo objeto
        pass

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "No se puede dividir por cero"

# Uso de la calculadora
mi_calculadora = Calculadora()

# Operaciones
resultado_suma = mi_calculadora.sumar(1, 1)
resultado_resta = mi_calculadora.restar(1, 1)
resultado_multiplicacion = mi_calculadora.multiplicar(1, 1)
resultado_division = mi_calculadora.dividir(1, 1)

# Mostrar resultados
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)


"""
En este ejemplo, hemos creado una clase llamada Calculadora. 
La clase tiene cuatro métodos (sumar, restar, multiplicar, dividir) que realizan operaciones básicas. 
El método __init__ es el constructor, que se llama automáticamente cuando se crea un objeto de la clase.

Luego, creamos una instancia de la clase Calculadora llamada mi_calculadora y utilizamos los métodos 
para realizar operaciones matemáticas.

La POO proporciona una forma de organizar y estructurar el código de manera más modular y reutilizable.
Cada instancia de la clase es un objeto independiente con su propio estado y comportamiento.
"""