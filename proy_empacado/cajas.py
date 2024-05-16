import sqlite3

# Función para crear la tabla de cajas si no existe
def crear_tabla():
    conn = sqlite3.connect('base_de_datos_cajas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cajas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            largo_caja INTEGER NOT NULL,
            ancho_caja INTEGER NOT NULL,
            alto_caja INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para añadir una nueva caja
def solicitar_datos_caja():
    while True:
        modelo = input("Ingrese el modelo de la caja: ")
        try:
            largo_caja = float(input("Ingrese el largo de la caja: "))
            ancho_caja = float(input("Ingrese el ancho de la caja: "))
            alto_caja = float(input("Ingrese el alto de la caja: "))
            return modelo, largo_caja, ancho_caja, alto_caja
        except ValueError:
            print("¡Error! Ha ingresado un tipo de valor incorrecto. Por favor, intente nuevamente.")

# Función para insertar una nueva caja en la base de datos
def añadir_caja(modelo, largo_caja, ancho_caja, alto_caja):
    conn = sqlite3.connect('base_de_datos_cajas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cajas (modelo, largo_caja, ancho_caja, alto_caja) VALUES (?, ?, ?, ?)', (modelo, largo_caja, ancho_caja, alto_caja))
    conn.commit()
    conn.close()

# Función para mostrar todas las cajas almacenadas
def mostrar_cajas():
    conn = sqlite3.connect('base_de_datos_cajas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cajas')
    cajas = cursor.fetchall()
    for caja in cajas:
        print(caja)
    conn.close()

# Lógica principal del programa
def main():
    crear_tabla()
    while True:
        print("\nBienvenido al sistema de gestión de cajas:")
        print("1) Mostrar cajas almacenadas")
        print("2) Añadir una nueva caja")
        print("3) Modificar una caja")
        print("4) Eliminar una caja")
        print("5) Salir y cerrar programa")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nCajas almacenadas:")
            mostrar_cajas()
        elif opcion == "2":
            modelo, largo_caja, ancho_caja, alto_caja = solicitar_datos_caja()
            añadir_caja(modelo, largo_caja, ancho_caja, alto_caja)
            print("¡Caja añadida exitosamente!")
        elif opcion == "3":
            pass  # Aquí iría la lógica para modificar una caja
        elif opcion == "4":
            pass  # Aquí iría la lógica para eliminar una caja
        elif opcion == "5":
            confirmacion = input("¿Estás seguro que deseas salir y cerrar el programa? (S/N): ")
            if confirmacion.lower() == "s":
                print("Cerrando programa...")
                break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
