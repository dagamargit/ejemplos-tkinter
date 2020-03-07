import tkinter as tk
from tkinter.messagebox import showinfo

class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.boton=tk.Button(self.ventana, text="Púlsame", command=self.saludar)
        self.boton.pack()

        self.ventana.mainloop()

    def saludar(self):
        showinfo(message="Me has pulsado")


aplicacion1=Aplicacion()