import sqlite3

# Función para conectar a la base de datos
def connect_to_database():
    conn = sqlite3.connect('boxes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS boxes (
                    id INTEGER PRIMARY KEY,
                    largo_interno REAL,
                    ancho_interno REAL,
                    alto_interno REAL,
                    espesor_material_largoyancho REAL,
                    espesor_material_alto REAL,
                    largo_externo REAL,
                    ancho_externo REAL,
                    alto_externo REAL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS changes (
                    id INTEGER PRIMARY KEY,
                    box_id INTEGER,
                    cambio TEXT,
                    FOREIGN KEY (box_id) REFERENCES boxes(id)
                )''')
    conn.commit()
    return conn, c

# Función para calcular dimensiones externas de la caja
def calcular_dimensiones_externas(largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto):
    largo_externo = largo_interno + espesor_material_largoyancho
    ancho_externo = ancho_interno + espesor_material_largoyancho
    alto_externo = alto_interno + espesor_material_alto
    return largo_externo, ancho_externo, alto_externo

# Función para crear una nueva caja y almacenar en la base de datos
def crear_caja(conn, c, largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto):
    try:
        # Validación de entradas no válidas
        if largo_interno <= 0 or ancho_interno <= 0 or alto_interno <= 0 or espesor_material_largoyancho <= 0 or espesor_material_alto <= 9: #antes: if largo_interno <= 0 or ancho_interno <= 0 or alto_interno <= 0 or espesor_material_largoyancho not in [5, 7] or espesor_material_alto != 9:
            print("Entradas no válidas. Verifique las dimensiones y el espesor del material.")
            return

        # Calcula las dimensiones externas
        largo_externo, ancho_externo, alto_externo = calcular_dimensiones_externas(largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto)

        # Inserta la nueva caja en la base de datos
        c.execute("INSERT INTO boxes (largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto, largo_externo, ancho_externo, alto_externo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto, largo_externo, ancho_externo, alto_externo))
        conn.commit()
        print("Caja creada exitosamente.")
    except Exception as e:
        print("Error al crear la caja:", str(e))

# Función para mostrar las cajas almacenadas en la base de datos
def mostrar_cajas(c):
    try:
        c.execute("SELECT * FROM boxes")
        boxes = c.fetchall()
        if not boxes:
            print("No hay cajas almacenadas.")
        else:
            print("Cajas almacenadas:")
            for box in boxes:
                print("ID:", box[0], "- Dimensiones internas:", box[1:4],"  -> espesores: ",box[5:6], " -> Dimensiones externas:", box[6:])
    except Exception as e:
        print("Error al mostrar las cajas:", str(e))

# Función para eliminar una caja por su ID
def eliminar_caja(conn, c, box_id):
    try:
        c.execute("DELETE FROM boxes WHERE id=?", (box_id,))
        conn.commit()
        print("Caja eliminada exitosamente.")
    except Exception as e:
        print("Error al eliminar la caja:", str(e))

# Función para editar las dimensiones de una caja existente
def editar_caja(conn, c, box_id, largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto):
    try:
        # Validación de entradas no válidas
        if largo_interno <= 0 or ancho_interno <= 0 or alto_interno <= 0 or espesor_material_largoyancho <= 0 or espesor_material_alto <= 9:
            print("Entradas no válidas. Verifique las dimensiones y el espesor del material.")
            return

        # Calcula las dimensiones externas
        largo_externo, ancho_externo, alto_externo = calcular_dimensiones_externas(largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto)

        # Actualiza la caja en la base de datos
        c.execute("UPDATE boxes SET largo_interno=?, ancho_interno=?, alto_interno=?, espesor_material_largoyancho=?, espesor_material_alto=?, largo_externo=?, ancho_externo=?, alto_externo=? WHERE id=?", (largo_interno, ancho_interno, alto_interno, espesor_material_largoyancho, espesor_material_alto, largo_externo, ancho_externo, alto_externo, box_id))
        conn.commit()
        print("Caja editada exitosamente.")
    except Exception as e:
        print("Error al editar la caja:", str(e))

# Función para almacenar el cambio de dimensiones en una caja
def almacenar_cambio_dimensiones(conn, c, box_id, cambio):
    try:
        # Verificar si hay más de 100 cambios, si es así, eliminar los más antiguos
        c.execute("SELECT COUNT(*) FROM changes WHERE box_id=?", (box_id,))
        count = c.fetchone()[0]
        if count >= 100:
            c.execute("DELETE FROM changes WHERE id IN (SELECT id FROM changes WHERE box_id=? ORDER BY id LIMIT ?)", (box_id, count - 99))

        # Almacenar el cambio de dimensiones en la base de datos
        c.execute("INSERT INTO changes (box_id, cambio) VALUES (?, ?)", (box_id, cambio))
        conn.commit()
    except Exception as e:
        print("Error al almacenar el cambio de dimensiones:", str(e))

# Función para cerrar la conexión con la base de datos
def cerrar_conexion(conn):
    conn.close()
    print("Conexión cerrada.")

# Función principal del programa
def main():
    # Conexión a la base de datos
    conn, c = connect_to_database()

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

if __name__ == "__main__":
    main()
