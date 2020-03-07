import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label=tk.Label(self.ventana, text="Hola Mundo")
        self.label.pack()
        self.ventana.mainloop()

aplicacion1=Aplicacion()