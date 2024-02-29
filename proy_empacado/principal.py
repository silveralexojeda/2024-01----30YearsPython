import sqlite3
from datetime import datetime

# Función para conectar con la base de datos de cajas
def conectar_base_datos_cajas():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    return conexion, cursor

# Función para conectar con la base de datos de filtros
def conectar_base_datos_filtros():
    conexion = sqlite3.connect('base_de_datos_filtros.db')
    cursor = conexion.cursor()
    return conexion, cursor

# Función para crear la tabla si no existe en la base de datos de asignaciones
def crear_tabla_asignaciones():
    conexion, cursor = conectar_base_datos_cajas()  # Corregido: Conectar a la base de datos de cajas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Empaquetado (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Filtro TEXT,
                        Caja TEXT,
                        Holgura FLOAT,
                        FechaHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conexion.commit()
    conexion.close()

# Función para mostrar todos los datos almacenados en la base de datos de asignaciones
def mostrar_asignaciones():
    conexion, cursor = conectar_base_datos_cajas()  # Corregido: Conectar a la base de datos de cajas
    cursor.execute("SELECT * FROM Empaquetado")
    asignaciones = cursor.fetchall()
    if asignaciones:
        print("Asignaciones resguardadas en la base de datos:")
        for asignacion in asignaciones:
            print(asignacion)
    else:
        print("No hay asignaciones resguardadas en la base de datos.")
    conexion.close()

# Función para realizar asignación caja a filtro
def asignar_caja_filtro(filtro):
    conexion_filtros, cursor_filtros = conectar_base_datos_filtros()
    cursor_filtros.execute("SELECT * FROM Filtros")
    filtros = cursor_filtros.fetchall()

    conexion_cajas, cursor_cajas = conectar_base_datos_cajas()
    cursor_cajas.execute("SELECT * FROM Cajas")
    cajas = cursor_cajas.fetchall()

    resultados = []
    for caja in cajas:
        for filtro_db in filtros:
            # Calcula la holgura entre el filtro y la caja
            holgura = calcular_holgura(filtro_db, caja)
            resultados.append((filtro_db, caja[1], holgura))  # Se agrega el ID de la caja

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
     # Convertir las dimensiones de filtro y caja a números
    filtro_dimensiones = tuple(map(int, filtro[1:]))
    caja_dimensiones = caja[1:]

    # Calcula las diferencias de dimensiones entre la caja y el filtro
    diferencia_largo = abs(caja_dimensiones[0] - filtro_dimensiones[0])
    diferencia_ancho = abs(caja_dimensiones[1] - filtro_dimensiones[1])
    diferencia_alto = abs(caja_dimensiones[2] - filtro_dimensiones[2])

    # Calcula la diferencia volumétrica
    diferencia_volumetrica_caja = caja_dimensiones[0] * caja_dimensiones[1] * caja_dimensiones[2]
    diferencia_volumetrica_filtro = filtro_dimensiones[0] * filtro_dimensiones[1] * filtro_dimensiones[2]
    diferencia_volumetrica = abs(diferencia_volumetrica_caja - diferencia_volumetrica_filtro)

    # Devuelve la menor de las diferencias como holgura
    holgura = min(diferencia_largo, diferencia_ancho, diferencia_alto, diferencia_volumetrica)
    return holgura

# Función para buscar todas las cajas
def buscar_todas_cajas():
    conexion, cursor = conectar_base_datos_cajas()
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
        print("3. Mostrar asignaciones resguardadas")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            filtro = input("Ingrese el filtro a asignar: ")
            asignar_caja_filtro(filtro)
        elif opcion == '2':
            buscar_todas_cajas()
        elif opcion == '3':
            mostrar_asignaciones()
        elif opcion == '4':
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
    crear_tabla_asignaciones()
    menu()

if __name__ == "__main__":
    main()
