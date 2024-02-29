import tkinter as tk
from tkinter import messagebox
import time
import random
import math

class MenuInterfaz:
    def __init__(self, master):
        self.master = master
        master.title("Menú de Prueba")

        self.label = tk.Label(master, text="Seleccione una opción:")
        self.label.pack()

        self.button1 = tk.Button(master, text="Prueba Colores", command=self.prueba_colores, font=("Helvetica", 20, "bold"))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(master, text="Segunda Opción", command=self.segunda_opcion, font=("Helvetica", 20, "bold"))
        self.button2.pack(pady=10)

        self.button3 = tk.Button(master, text="Salir", command=self.salir, font=("Helvetica", 20, "bold"))
        self.button3.pack(pady=10)

    def prueba_colores(self):
        self.label.config(text="Hola", font=("Helvetica", 100, "bold"))
        self.cambiar_color()

    def cambiar_color(self):
        color = self.generar_color()
        self.label.config(fg=color)
        self.master.after(100, self.cambiar_color)

    def segunda_opcion(self):
        self.label.config(text="Generando formas...", font=("Helvetica", 20, "italic"))
        self.mostrar_formas()

    def mostrar_formas(self):
        for _ in range(10):
            self.dibujar_forma()
            time.sleep(0.5)
            self.label.update()

    def dibujar_forma(self):
        canvas = tk.Canvas(self.master, width=200, height=200)
        canvas.pack()
        
        num_lados = random.randint(4, 10)
        centro_x = 100
        centro_y = 100
        radio = 80
        puntos = []
        for i in range(num_lados):
            angulo = 2 * i * math.pi / num_lados
            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)
            puntos.extend([x, y])

        canvas.create_polygon(puntos, fill=self.generar_color(), outline='black', width=2)

    def salir(self):
        confirmacion = tk.messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
        if confirmacion:
            self.master.destroy()

    def generar_color(self):
        # Genera un color hexadecimal aleatorio
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

root = tk.Tk()
root.geometry("800x600")
menu = MenuInterfaz(root)
root.mainloop()
