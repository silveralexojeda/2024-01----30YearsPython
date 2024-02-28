import sqlite3

# Función para crear la tabla de filtros si no existe
def crear_tabla():
    conn = sqlite3.connect('base_de_datos_filtros.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filtros (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            tipo TEXT NOT NULL,
            tamaño INTEGER NOT NULL,
            material TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para añadir un nuevo filtro
def añadir_filtro(nombre, tipo, tamaño, material):
    conn = sqlite3.connect('base_de_datos_filtros.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO filtros (nombre, tipo, tamaño, material) VALUES (?, ?, ?, ?)', (nombre, tipo, tamaño, material))
    conn.commit()
    conn.close()

# Función para mostrar todos los filtros almacenados
def mostrar_filtros():
    conn = sqlite3.connect('base_de_datos_filtros.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM filtros')
    filtros = cursor.fetchall()
    for filtro in filtros:
        print(filtro)
    conn.close()

# Lógica principal del programa
def main():
    crear_tabla()
    while True:
        print("\nBienvenido al sistema de gestión de filtros:")
        print("1) Mostrar filtros almacenados")
        print("2) Añadir un nuevo filtro")
        print("3) Modificar un filtro")
        print("4) Eliminar un filtro")
        print("5) Salir y cerrar programa")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nFiltros almacenados:")
            mostrar_filtros()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del filtro: ")
            tipo = input("Ingrese el tipo del filtro: ")
            tamaño = int(input("Ingrese el tamaño del filtro: "))
            material = input("Ingrese el material del filtro: ")
            añadir_filtro(nombre, tipo, tamaño, material)
            print("¡Filtro añadido exitosamente!")
        elif opcion == "3":
            pass  # Aquí iría la lógica para modificar un filtro
        elif opcion == "4":
            pass  # Aquí iría la lógica para eliminar un filtro
        elif opcion == "5":
            confirmacion = input("¿Estás seguro que deseas salir y cerrar el programa? (S/N): ")
            if confirmacion.lower() == "s":
                print("Cerrando programa...")
                break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
