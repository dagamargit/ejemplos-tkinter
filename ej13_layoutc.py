import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("800x600")
        self.ventana1.resizable(0,0)
        self.boton1=ttk.Button(self.ventana1, text="Confirmar")
        self.boton1.place(x=680, y=550, width=90, height=30)
        self.boton2=ttk.Button(self.ventana1, text="Cancelar")
        self.boton2.place(x=580, y=550, width=90, height=30)
        self.ventana1.mainloop()

aplicacion1=Aplicacion()