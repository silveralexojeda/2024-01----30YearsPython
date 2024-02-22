import sqlite3

class Filtro:
    def __init__(self, modelo, largo, ancho, alto):
        self.modelo = modelo
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

def crear_tabla():
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS filtros
                 (modelo TEXT, largo REAL, ancho REAL, alto REAL)''')
    conn.commit()
    conn.close()

def agregar_filtro(filtro):
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()
    c.execute("INSERT INTO filtros VALUES (?, ?, ?, ?)",
              (filtro.modelo, filtro.largo, filtro.ancho, filtro.alto))
    conn.commit()
    conn.close()

def imprimir_filtros():
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()
    c.execute("SELECT * FROM filtros")
    filtros = c.fetchall()
    conn.close()
    if not filtros:
        print("No hay filtros en la base de datos.")
    else:
        print("Lista de filtros:")
        for filtro in filtros:
            print(f"Modelo: {filtro[0]}, Largo: {filtro[1]}, Ancho: {filtro[2]}, Alto: {filtro[3]}")

def agregar_nuevo_filtro():
    modelo = input("Ingrese el modelo del nuevo filtro: ")
    largo = float(input("Ingrese el largo del nuevo filtro: "))
    ancho = float(input("Ingrese el ancho del nuevo filtro: "))
    alto = float(input("Ingrese el alto del nuevo filtro: "))

    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()

    # Verificar si ya existe un filtro con el mismo modelo
    c.execute("SELECT * FROM filtros WHERE modelo=?", (modelo,))
    existing_filtro = c.fetchone()

    # Verificar si ya existe un filtro con las mismas dimensiones
    c.execute("SELECT * FROM filtros WHERE largo=? AND ancho=? AND alto=?", (largo, ancho, alto))
    same_dimensions_filtro = c.fetchone()

    conn.close()

    if existing_filtro:
        print(f"Ya existe un filtro con el modelo '{modelo}'.")
    elif same_dimensions_filtro:
        print(f"Ya existe un filtro con las mismas dimensiones: Largo: {largo}, Ancho: {ancho}, Alto: {alto}.")
    else:
        nuevo_filtro = Filtro(modelo, largo, ancho, alto)
        agregar_filtro(nuevo_filtro)
        print("El nuevo filtro ha sido agregado correctamente.")

def depurar_base_datos():
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()
    c.execute("DELETE FROM filtros WHERE ROWID NOT IN (SELECT ROWID FROM filtros ORDER BY ROWID DESC LIMIT 3)")
    conn.commit()
    conn.close()
    print("La base de datos ha sido depurada a 3 filtros.")

def agregar_filtros_iniciales(filtros):
    conn = sqlite3.connect('filtros.db')
    c = conn.cursor()

    for filtro in filtros:
        # Verificar si el filtro ya existe en la base de datos
        c.execute("SELECT * FROM filtros WHERE modelo=?", (filtro.modelo,))
        existing_filtro = c.fetchone()
        if not existing_filtro:
            agregar_filtro(filtro)
            print(f"El filtro '{filtro.modelo}' ha sido agregado a la base de datos.")
        else:
            print(f"El filtro '{filtro.modelo}' ya existe en la base de datos. No se agregó nuevamente.")

    conn.close()

def main():
    crear_tabla()

    filtros = [
        Filtro("Filtro1", 10, 5, 3),
        Filtro("Filtro2", 8, 6, 4),
        Filtro("Filtro3", 12, 7, 5),
        Filtro("Filtro4", 9, 5, 2),
        Filtro("Filtro5", 11, 8, 6)
    ]

    agregar_filtros_iniciales(filtros)

    imprimir_filtros()

    while True:
        agregar_otro = input("¿Desea agregar otro filtro? (S/N): ").strip().lower()
        if agregar_otro != 's':
            if input("¿Desea depurar la base de datos a 3 filtros? (S/N): ").strip().lower() == 's':
                depurar_base_datos()
                imprimir_filtros()
            break
        agregar_nuevo_filtro()
        imprimir_filtros()

if __name__ == "__main__":
    main()
