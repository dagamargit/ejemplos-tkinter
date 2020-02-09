import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Rojo", command=self.fijarrojo, accelerator="Ctrl+R")
        opciones1.add_command(label="Verde", command=self.fijarverde, accelerator="Ctrl+V")
        opciones1.add_separator()        
        opciones1.add_command(label="Azul", command=self.fijarazul, accelerator="Ctrl+A")
        self.ventana1.bind_all("<Control-r>", self.cambiar)
        self.ventana1.bind_all("<Control-v>", self.cambiar)
        self.ventana1.bind_all("<Control-a>", self.cambiar)
        menubar1.add_cascade(label="Colores", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)        
        self.ventana1.mainloop()

    def cambiar(self, event):
        if event.keysym=="r":
            self.fijarrojo()
        if event.keysym=="v":
            self.fijarverde()
        if event.keysym=="a":
            self.fijarazul()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

aplicacion1=Aplicacion()