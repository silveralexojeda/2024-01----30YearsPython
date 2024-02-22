import time

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
            self.numero1 = float(input("*Ingrese el primer número: "))
            self.numero2 = float(input("**Ingrese el segundo número: "))
        except ValueError:
            for _ in range(50):
                print("Error404: No seas pendejo.")
                wait_time = 0.025 #ESPEPRA # SEGUNDO
                time.sleep(wait_time)
            print("\n"*100)
            mi_calculadora.solicitar_numeros()

    def limpiar_terminal(self):
        # Método para limpiar la terminal
        #subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
        print("\n"*100)

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
    
    def cuadrado(self):
        return self.numero1 * self.numero1

# Ciclo principal
while True:
    # Uso de la calculadora
    #crea objeto mi_calculadora / variable con valor tipo class
    mi_calculadora = Calculadora()
    segunda_calculadora = Calculadora()
    
    

    # Limpiar la terminal
    mi_calculadora.limpiar_terminal()

    # Solicitar números al usuario
    mi_calculadora.solicitar_numeros()
    
    



    # Operaciones
    resultado_suma = mi_calculadora.sumar()
    resultado_resta = mi_calculadora.restar()
    resultado_multiplicacion = mi_calculadora.multiplicar()
    
    resultado_division = mi_calculadora.dividir()
    
    resultado_cuadrados=mi_calculadora.cuadrado()

    
    
    # Mostrar resultados
    print("\n"*100)
    print("**************************************************") #50 * y 35+13=48
    #print("la longitud de: ",str(resultado_suma),"  es:",len(str(resultado_suma)))
    print("||Suma:", resultado_suma," "*(38-len(str(resultado_suma))),"||")
    print("||Resta:", resultado_resta," "*(37-len(str(resultado_resta))),"||")
    print("||Multiplicación:", resultado_multiplicacion," "*(28-len(str(resultado_multiplicacion))),"||")
    print("||División:", resultado_division, " "*(34-len(str(resultado_division))),"||")
    print("||el resultado del cuadrado del primer numero es: ",resultado_cuadrados," "*(34-len(str(resultado_division))),"||")
    print("**************************************************\n")

    # Preguntar si desea salir
    #print("\nPresiona 'Esc' para salir, o cualquier otra tecla para continuar.")
    #if keyboard.read_event().name == 'esc':

    x = input("presione x + enter para salir\n")
    if "x" == x:
        break