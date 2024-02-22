import sqlite3

class Caja:
    def __init__(self, modelo, largo, ancho, alto):
        self.modelo = modelo
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

class Filtro:
    def __init__(self, modelo, largo, ancho, alto):
        self.modelo = modelo
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

def crear_tabla_cajas():
    conn = sqlite3.connect('cajas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cajas
                 (modelo TEXT, largo REAL, ancho REAL, alto REAL)''')
    conn.commit()
    conn.close()

def crear_tabla_filtros():
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS filtros
                 (modelo TEXT, largo REAL, ancho REAL, alto REAL)''')
    conn.commit()
    conn.close()

def crear_tabla_relaciones():
    conn = sqlite3.connect('relaciones.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS relaciones
                 (filtro_modelo TEXT, caja_modelo TEXT)''')
    conn.commit()
    conn.close()

def agregar_filtro_si_no_existe(modelo, largo, ancho, alto):
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()
    c.execute("SELECT * FROM filtros WHERE modelo=?", (modelo,))
    existing_filtro = c.fetchone()
    if not existing_filtro:
        c.execute("INSERT INTO filtros VALUES (?, ?, ?, ?)", (modelo, largo, ancho, alto))
        conn.commit()
        print(f"El filtro '{modelo}' ha sido agregado a la base de datos de filtros.")
    conn.close()

def obtener_cajas_disponibles(filtro):
    conn = sqlite3.connect('cajas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cajas WHERE largo >= ? AND ancho >= ? AND alto >= ?",
              (filtro.largo + 2, filtro.ancho + 2, filtro.alto + 2))
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

def agregar_nueva_caja(modelo, largo, ancho, alto):
    conn = sqlite3.connect('cajas.db')
    c = conn.cursor()
    c.execute("INSERT INTO cajas VALUES (?, ?, ?, ?)", (modelo, largo, ancho, alto))
    conn.commit()
    conn.close()
    print(f"Se ha creado una nueva caja '{modelo}'.")

def relacionar_filtro_y_caja(filtro_modelo, caja_modelo):
    conn = sqlite3.connect('relaciones.db')
    c = conn.cursor()
    c.execute("INSERT INTO relaciones VALUES (?, ?)", (filtro_modelo, caja_modelo))
    conn.commit()
    conn.close()
    print(f"Se ha relacionado el filtro '{filtro_modelo}' con la caja '{caja_modelo}'.")

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

    modelo = input("Ingrese el modelo del filtro: ")
    largo = float(input("Ingrese el largo del filtro: "))
    ancho = float(input("Ingrese el ancho del filtro: "))
    alto = float(input("Ingrese el alto del filtro: "))

    filtro = Filtro(modelo, largo, ancho, alto)

    agregar_filtro_si_no_existe(modelo, largo, ancho, alto)

    caja_disponible = seleccionar_caja_disponible(filtro)

    if caja_disponible:
        relacionar_filtro_y_caja(modelo, caja_disponible[0])
        print(f"Se ha seleccionado la caja '{caja_disponible[0]}' para el filtro '{modelo}'.")
    else:
        print("No hay cajas disponibles con las dimensiones requeridas.")
        nuevo_modelo_caja = input("Ingrese el modelo de la nueva caja: ")
        largo_caja = float(input("Ingrese el largo de la nueva caja: "))
        ancho_caja = float(input("Ingrese el ancho de la nueva caja: "))
        alto_caja = float(input("Ingrese el alto de la nueva caja: "))
        agregar_nueva_caja(nuevo_modelo_caja, largo_caja, ancho_caja, alto_caja)
        relacionar_filtro_y_caja(modelo, nuevo_modelo_caja)

    mostrar_relaciones()

if __name__ == "__main__":
    main()
