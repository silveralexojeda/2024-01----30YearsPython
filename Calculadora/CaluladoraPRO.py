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
 
     def __init__(self, valor1, valor2):
        # Constructor: se llama cuando se crea un nuevo objeto
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self, num1, num2):
        return num1 + num2
    #Comparar esta opcion con la anterior solo colcando valores fijos a las operaciones, 
    #lon  nuevo es con variables
    def sumar(self):
        return self.valor1 + self.valor2

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








------------------
En la programación orientada a objetos, 
el constructor es un método especial que se llama automáticamente cuando se crea una instancia (objeto) de la clase. 
En Python, el constructor se define utilizando el método __init__. 
El propósito principal del constructor es inicializar los atributos del objeto y realizar cualquier configuración necesaria 
durante la creación.

En el ejemplo de la calculadora que proporcioné anteriormente, el constructor se define así:

** python ** ** Copy code
def __init__(self):
    # Constructor: se llama cuando se crea un nuevo objeto
    pass

En este caso, el constructor no realiza ninguna acción específica, ya que simplemente contiene la instrucción pass, 
que es una instrucción nula en Python. Sin embargo, es común incluir el constructor incluso si no realiza ninguna acción, 
ya que es un lugar donde se pueden inicializar atributos de la instancia.

Si nuestra calculadora tuviera atributos que necesitaran ser inicializados durante la creación del objeto, podríamos hacerlo dentro del constructor. Por ejemplo, si quisiéramos tener una variable que almacene el número total de operaciones realizadas, podríamos modificar el constructor de la siguiente manera:
Ejemplo: 
def __init__(self):
    # Constructor: se llama cuando se crea un nuevo objeto
    self.total_operaciones = 0

En este caso, cada vez que se crea una nueva instancia de la clase Calculadora, se inicializa el atributo total_operaciones en 0.

La estructura de la clase en este ejemplo sigue un patrón común en la programación orientada a objetos:

Atributos: Son las variables asociadas a la clase. En este caso, no tenemos atributos, pero podríamos agregarlos según sea necesario.

Constructor (__init__): Se utiliza para inicializar los atributos de la instancia. En este ejemplo, no se inicializan atributos, pero podríamos hacerlo si fuera necesario.

Métodos: Son las funciones asociadas a la clase. En este caso, los métodos (sumar, restar, multiplicar, dividir) realizan operaciones matemáticas básicas.

La programación orientada a objetos proporciona una forma de encapsular datos y funcionalidades relacionadas en un solo objeto, lo que facilita la organización y mantenimiento del código.







"""