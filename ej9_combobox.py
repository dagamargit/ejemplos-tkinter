import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Seleccione un día de la semana")
        self.label1.grid(column=0, row=0)
        self.opcion=tk.StringVar()
        diassemana=("lunes","martes","miércoles","jueves","viernes","sábado","domingo")
        self.combobox1=ttk.Combobox(self.ventana1, 
                                  width=10, 
                                  textvariable=self.opcion, 
                                  values=diassemana,
                                  state='readonly')
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=2)
        self.label2=ttk.Label(self.ventana1, text="Día seleccionado:")
        self.label2.grid(column=0, row=3)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.configure(text=self.opcion.get())

aplicacion1=Aplicacion()