import sqlite3
from datetime import datetime

# Función para conectar con la base de datos
def conectar_base_datos():
    conexion = sqlite3.connect('Seleccion_y_relaciones.db')
    cursor = conexion.cursor()
    return conexion, cursor

# Función para crear la tabla si no existe
def crear_tabla():
    conexion, cursor = conectar_base_datos()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Empaquetado (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Filtro TEXT,
                        Caja TEXT,
                        Holgura FLOAT,
                        FechaHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conexion.commit()
    conexion.close()

# Función para mostrar todos los datos almacenados
def mostrar_datos():
    conexion, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM Empaquetado")
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
    conexion.close()

# Función para realizar asignación caja a filtro
def asignar_caja_filtro(filtro):
    conexion, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM Cajas")
    cajas = cursor.fetchall()

    resultados = []
    for caja in cajas:
        # Calcula la holgura entre el filtro y la caja
        holgura = calcular_holgura(filtro, caja)
        resultados.append((filtro, caja[1], holgura))  # Se agrega el ID de la caja

    for resultado in resultados:
        print(resultado)

    confirmacion = input("¿Estás de acuerdo con los resultados? (Sí/No): ")
    if confirmacion.lower() == 'si':
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for resultado in resultados:
            # Agrega la fecha y hora de la asignación al registro del mensaje empaquetado
            mensaje = resultado[1] + ", asignado el " + fecha_hora
            cursor.execute("INSERT INTO Empaquetado (Filtro, Caja, Holgura, FechaHora) VALUES (?, ?, ?, ?)", (filtro, mensaje, resultado[2], fecha_hora))
        conexion.commit()
        print("Datos guardados exitosamente.")
    else:
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensaje = "No se ha localizado caja para este filtro, último intento realizado el " + fecha_hora
        print(mensaje)
        cursor.execute("INSERT INTO Empaquetado (Filtro, Caja, Holgura, FechaHora) VALUES (?, ?, ?, ?)", (filtro, mensaje, 0, fecha_hora))
        conexion.commit()

    conexion.close()

# Función para calcular la holgura entre el filtro y la caja
def calcular_holgura(filtro, caja):
    # Calcula las diferencias de dimensiones entre la caja y el filtro
    diferencia_largo = abs(caja[1] - filtro[1])
    diferencia_ancho = abs(caja[2] - filtro[2])
    diferencia_alto = abs(caja[3] - filtro[3])

    # Calcula la diferencia volumétrica
    diferencia_volumetrica_caja = caja[1] * caja[2] * caja[3]
    diferencia_volumetrica_filtro = filtro[1] * filtro[2] * filtro[3]
    diferencia_volumetrica = abs(diferencia_volumetrica_caja - diferencia_volumetrica_filtro)

    # Devuelve la menor de las diferencias como holgura
    holgura = min(diferencia_largo, diferencia_ancho, diferencia_alto, diferencia_volumetrica)
    return holgura

# Función para buscar todas las cajas
def buscar_todas_cajas():
    conexion, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM Cajas")
    cajas = cursor.fetchall()

    # Realiza algún procesamiento con las cajas encontradas
    for caja in cajas:
        # Implementa cualquier lógica adicional aquí
        print(caja)

    print("Búsqueda de cajas completada.")
    conexion.close()

# Función principal para mostrar el menú
def menu():
    while True:
        print("\n---- Menú ----")
        print("1. Realizar asignación caja a filtro")
        print("2. Buscar todas las cajas")
        print("3. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            filtro = input("Ingrese el filtro a asignar: ")
            asignar_caja_filtro(filtro)
        elif opcion == '2':
            buscar_todas_cajas()
        elif opcion == '3':
            confirmacion = input("¿Está seguro de que desea salir del programa? (Sí/No): ")
            if confirmacion.lower() == 'si':
                print("Saliendo del programa...")
                break
            else:
                continue
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Función principal para ejecutar el programa
def main():
    crear_tabla()
    menu()

if __name__ == "__main__":
    main()
