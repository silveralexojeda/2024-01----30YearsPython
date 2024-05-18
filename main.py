from pathlib import Path
from Nuevo_Proyecto_cajas_V2.Administrador_cajas import connect_to_database, crear_caja, mostrar_cajas, eliminar_caja, editar_caja, almacenar_cambio_dimensiones, cerrar_conexion

# database_filepath = Path("./Nuevo_Proyecto_cajas_V2/boxes.db").resolve()
database_filepath = Path("./boxes.db").resolve()
# Conexión a la base de datos
conn, c = connect_to_database(database_filepath)

while True:
    print("\nMenú:")
    print("1. Crear nueva caja")
    print("2. Mostrar cajas almacenadas")
    print("3. Eliminar caja")
    print("4. Editar caja")
    print("5. Cerrar programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nCreación de nueva caja:")
        largo_interno = float(input("Ingrese el largo interno de la caja (en mm): "))
        ancho_interno = float(input("Ingrese el ancho interno de la caja (en mm): "))
        alto_interno = float(input("Ingrese el alto interno de la caja (en mm): "))
        espesor_material_largoyancho = float(input("Ingrese el espesor del material para largo y ancho (5 o 7 mm): "))
        espesor_material_alto = float(input("Ingrese el espesor del material para alto (9 mm): "))
        crear_caja(conn, c, largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto)
    elif opcion == "2":
        print("\nCajas almacenadas:")
        mostrar_cajas(c)
    elif opcion == "3":
        box_id = int(input("Ingrese el ID de la caja que desea eliminar: "))
        eliminar_caja(conn, c, box_id)
    elif opcion == "4":
        box_id = int(input("Ingrese el ID de la caja que desea editar: "))
        # Solicitar las nuevas dimensiones de la caja
        nuevo_largo_interno = float(input("Ingrese el nuevo largo interno de la caja (en mm): "))
        nuevo_ancho_interno = float(input("Ingrese el nuevo ancho interno de la caja (en mm): "))
        nuevo_alto_interno = float(input("Ingrese el nuevo alto interno de la caja (en mm): "))
        nuevo_espesor_material_largoyancho = float(input("Ingrese el nuevo espesor del material para largo y ancho (5 o 7 mm): "))
        nuevo_espesor_material_alto = float(input("Ingrese el nuevo espesor del material para alto (9 mm): "))
        # Editar la caja con las nuevas dimensiones
        editar_caja(conn, c, box_id, nuevo_largo_interno, nuevo_ancho_interno, nuevo_alto_interno, nuevo_espesor_material_largoyancho, nuevo_espesor_material_alto)
        # Almacenar el cambio de dimensiones
        cambio_dimensiones = f"Se editó la caja {box_id} con nuevas dimensiones: largo={nuevo_largo_interno}mm, ancho={nuevo_ancho_interno}mm, alto={nuevo_alto_interno}mm."
        almacenar_cambio_dimensiones(conn, c, box_id, cambio_dimensiones)
    elif opcion == "5":
        cerrar_conexion(conn)
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
