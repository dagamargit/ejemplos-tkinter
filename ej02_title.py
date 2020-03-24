import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=1)
        self.ventana1.mainloop()

    def ingresar(self):
        self.ventana1.title(self.dato.get())

aplicacion1=Aplicacion()