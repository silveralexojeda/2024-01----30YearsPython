import sqlite3
from datetime import datetime

# Función para conectar con la base de datos
def conectar_base_datos():
    conexion = sqlite3.connect('base_de_datos_empacado.db')
    cursor = conexion.cursor()
    return conexion, cursor

# Función para crear la tabla si no existe
def crear_tabla():
    conexion, cursor = conectar_base_datos()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Empaquetado (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Filtro TEXT,
                        Opcion INTEGER,
                        Caja TEXT,
                        Holgura FLOAT,
                        FechaHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conexion.commit()
    conexion.close()

# Función para realizar una asignación de caja a filtro
def asignar_caja_filtro():
    conexion, cursor = conectar_base_datos()

    # Realizar iteración entre las dimensiones de las cajas y los filtros
    cursor.execute("SELECT * FROM base_de_datos_cajas")
    cajas = cursor.fetchall()

    cursor.execute("SELECT * FROM base_de_datos_filtros")
    filtros = cursor.fetchall()

    resultados = []
    for caja in cajas:
        for filtro in filtros:
            # Aquí se puede realizar el cálculo de si el filtro cabe en la caja y guardar la información

    # Código para guardar los resultados en la base de datos Empaquetado

    conexion.close()

# Función para mostrar todas las asignaciones
def mostrar_asignaciones():
    conexion, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM Empaquetado")
    asignaciones = cursor.fetchall()
    for asignacion in asignaciones:
        print(asignacion)
    conexion.close()

# Menú principal
def menu():
    while True:
        print("\n---- Menú ----")
        print("1. Realizar asignación caja a filtro")
        print("2. Buscar todas las cajas")
        print("3. Mostrar asignaciones resguardadas")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            asignar_caja_filtro()
        elif opcion == '2':
            # Agregar función para buscar todas las cajas
            pass
        elif opcion == '3':
            mostrar_asignaciones()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Función principal para ejecutar el programa
def main():
    crear_tabla()
    menu()

if __name__ == "__main__":
    main()

