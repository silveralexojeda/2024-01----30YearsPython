import sqlite3

class Caja:
    def __init__(self, id, largo_interno, ancho_interno, alto_interno):
        self.id = id
        self.largo_interno = largo_interno
        self.ancho_interno = ancho_interno
        self.alto_interno = alto_interno

class Filtro:
    def __init__(self, id, largo_interno, ancho_interno, alto_interno):
        self.id = id
        self.largo_interno = largo_interno
        self.ancho_interno = ancho_interno
        self.alto_interno = alto_interno

def crear_tabla_cajas():
    conn = sqlite3.connect("C:\\Users\\silve\\Videos\\visual studio code\\2024-01----30DaysPython\\2024-01----30YearsPython\\Nuevo_Proyecto_cajas_V2\\cajasV2.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cajas
                 (id TEXT, largo_interno REAL, ancho_interno REAL, alto_interno REAL)''')
    conn.commit()
    conn.close()

def crear_tabla_filtros():
    conn = sqlite3.connect("C:\\Users\\silve\\Videos\\visual studio code\\2024-01----30DaysPython\\2024-01----30YearsPython\\Nuevo_Proyecto_cajas_V2\\filtrosV2.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS filtros
                 (id TEXT, largo_interno REAL, ancho_interno REAL, alto_interno REAL)''')
    conn.commit()
    conn.close()

def crear_tabla_relaciones():
    conn = sqlite3.connect('relaciones.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS relaciones
                 (filtro_id TEXT, caja_id TEXT)''')
    conn.commit()
    conn.close()

def agregar_filtro_si_no_existe(id, largo_interno, ancho_interno, alto_interno):
    conn = sqlite3.connect("C:\\Users\\silve\\Videos\\visual studio code\\2024-01----30DaysPython\\2024-01----30YearsPython\\Nuevo_Proyecto_cajas_V2\\filtrosV2.db")
    c = conn.cursor()
    c.execute("SELECT * FROM filtros WHERE id=?", (id,))
    existing_filtro = c.fetchone()
    if not existing_filtro:
        c.execute("INSERT INTO filtros VALUES (?, ?, ?, ?)", (id, largo_interno, ancho_interno, alto_interno))
        conn.commit()
        print(f"El filtro '{id}' ha sido agregado a la base de datos de filtros.")
    conn.close()

def obtener_cajas_disponibles(filtro):
    conn = sqlite3.connect("C:\\Users\\silve\\Videos\\visual studio code\\2024-01----30DaysPython\\2024-01----30YearsPython\\Nuevo_Proyecto_cajas_V2\\cajasV2.db")
    c = conn.cursor()
    c.execute("SELECT * FROM cajas WHERE largo_interno >= ? AND ancho_interno >= ? AND alto_interno >= ?",
              (filtro.largo_interno + 2, filtro.ancho_interno + 2, filtro.alto_interno + 2))
    cajas = c.fetchall()
    conn.close()
    return cajas

def seleccionar_caja_disponible(filtro):
    cajas = obtener_cajas_disponibles(filtro)
    if cajas:
        # Seleccionar la primera caja disponible
        return cajas[0]
    else:
        return None

def agregar_nueva_caja(id, largo_interno, ancho_interno, alto_interno):
    conn = sqlite3.connect("C:\\Users\\silve\\Videos\\visual studio code\\2024-01----30DaysPython\\2024-01----30YearsPython\\Nuevo_Proyecto_cajas_V2\\cajasV2.db")
    c = conn.cursor()
    c.execute("INSERT INTO cajas VALUES (?, ?, ?, ?)", (id, largo_interno, ancho_interno, alto_interno))
    conn.commit()
    conn.close()
    print(f"Se ha creado una nueva caja '{id}'.")

def relacionar_filtro_y_caja(filtro_id, caja_id):
    conn = sqlite3.connect('relaciones.db')
    c = conn.cursor()
    c.execute("INSERT INTO relaciones VALUES (?, ?)", (filtro_id, caja_id))
    conn.commit()
    conn.close()
    print(f"Se ha relacionado el filtro '{filtro_id}' con la caja '{caja_id}'.")

def mostrar_relaciones():
    conn = sqlite3.connect('relaciones.db')
    c = conn.cursor()
    c.execute("SELECT * FROM relaciones")
    relaciones = c.fetchall()
    conn.close()
    if not relaciones:
        print("No hay relaciones almacenadas en la base de datos.")
    else:
        print("Relaciones entre filtros y cajas:")
        for relacion in relaciones:
            print(f"Filtro: {relacion[0]}, Caja: {relacion[1]}")

def main():
    crear_tabla_cajas()
    crear_tabla_filtros()
    crear_tabla_relaciones()

    id = input("Ingrese el id del filtro: ")
    largo_interno = float(input("Ingrese el largo_interno del filtro: "))
    ancho_interno = float(input("Ingrese el ancho_interno del filtro: "))
    alto_interno = float(input("Ingrese el alto_interno del filtro: "))

    filtro = Filtro(id, largo_interno, ancho_interno, alto_interno)

    agregar_filtro_si_no_existe(id, largo_interno, ancho_interno, alto_interno)

    caja_disponible = seleccionar_caja_disponible(filtro)

    if caja_disponible:
        relacionar_filtro_y_caja(id, caja_disponible[0])
        print(f"Se ha seleccionado la caja '{caja_disponible[0]}' para el filtro '{id}'.")
    else:
        print("No hay cajas disponibles con las dimensiones requeridas.")
        nuevo_id_caja = input("Ingrese el id de la nueva caja: ")
        largo_interno_caja = float(input("Ingrese el largo_interno de la nueva caja: "))
        ancho_interno_caja = float(input("Ingrese el ancho_interno de la nueva caja: "))
        alto_interno_caja = float(input("Ingrese el alto_interno de la nueva caja: "))
        agregar_nueva_caja(nuevo_id_caja, largo_interno_caja, ancho_interno_caja, alto_interno_caja)
        relacionar_filtro_y_caja(id, nuevo_id_caja)

    mostrar_relaciones()

if __name__ == "__main__":
    main()
