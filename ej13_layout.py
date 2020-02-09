import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1, text="Boton 1")
        self.boton1.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton2=ttk.Button(self.ventana1, text="Boton 2")
        self.boton2.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton3=ttk.Button(self.ventana1, text="Boton 3")
        self.boton3.pack(side=tk.TOP, fill=tk.BOTH)

        # Si agrandamos la ventana podemos ver que el botón fijado a izquierda siempre permanece en dicho lugar y los fijados a derecha se desplazan:
        self.boton4=ttk.Button(self.ventana1, text="Boton 4")
        self.boton4.pack(side=tk.LEFT)
        self.boton5=ttk.Button(self.ventana1, text="Boton 5")
        self.boton5.pack(side=tk.RIGHT)
        self.boton6=ttk.Button(self.ventana1, text="Boton 6")
        self.boton6.pack(side=tk.RIGHT)
        self.boton7=ttk.Button(self.ventana1, text="Boton 7")
        self.boton7.pack(side=tk.RIGHT)
        self.ventana1.mainloop()

aplicacion1=Aplicacion()