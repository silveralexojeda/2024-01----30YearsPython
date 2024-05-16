import sqlite3

# Función para conectar a la base de datos
def connect_to_database():
    conn = sqlite3.connect('boxes.db')
    c = conn.cursor()
    return conn, c

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

# Función para cerrar la conexión con la base de datos
def cerrar_conexion(conn):
    conn.close()
    print("Conexión cerrada.")

# Función principal del programa
def main():
    # Conexión a la base de datos
    conn, c = connect_to_database()

    # Mostrar las cajas almacenadas
    mostrar_cajas(c)

    # Cerrar conexión
    cerrar_conexion(conn)

if __name__ == "__main__":
    main()