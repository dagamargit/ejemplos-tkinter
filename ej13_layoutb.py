import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1, text="Boton 1")
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.ventana1, text="Boton 2")
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.ventana1, text="Boton 3")
        self.boton3.grid(column=2, row=0, rowspan=2, sticky="ns") # sticky para que ocupe todo
        self.boton4=ttk.Button(self.ventana1, text="Boton 4")
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.ventana1, text="Boton 5")
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.ventana1, text="Boton 6")
        self.boton6.grid(column=0, row=2, columnspan=3, sticky="we") # west to east
        self.ventana1.mainloop()

aplicacion1=Aplicacion()