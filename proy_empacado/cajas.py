import sqlite3

# Función para crear la tabla de cajas si no existe
def crear_tabla():
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cajas (
            id INTEGER PRIMARY KEY,
            modelo TEXT NOT NULL,
            largo INTEGER NOT NULL,
            ancho INTEGER NOT NULL,
            alto INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para añadir una nueva caja
def añadir_caja(modelo, largo, ancho, alto):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cajas (modelo, largo, ancho, alto) VALUES (?, ?, ?, ?)', (modelo, largo, ancho, alto))
    conn.commit()
    conn.close()

# Función para mostrar todas las cajas almacenadas
def mostrar_cajas():
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cajas')
    cajas = cursor.fetchall()
    for caja in cajas:
        print(caja)
    conn.close()
    print("\n\n\n")

# Lógica principal del programa
def main():
    crear_tabla()
    mostrar_cajas()
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
            modelo = input("Ingrese el modelo de la caja: ")
            largo = int(input("Ingrese el largo de la caja: "))
            ancho = int(input("Ingrese el ancho de la caja: "))
            alto = int(input("Ingrese el alto de la caja: "))
            añadir_caja(modelo, largo, ancho, alto)
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
