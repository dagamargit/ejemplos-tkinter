import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Rojo", command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        submenu1=tk.Menu(menubar1)
        submenu1.add_command(label="1024x1024", command=self.tamano1)
        submenu1.add_command(label="1280x1024", command=self.tamano2)        
        opciones2.add_cascade(label="Otros tamaños", menu= submenu1)        
        menubar1.add_cascade(label="Tamaños", menu=opciones2)        
        self.ventana1.mainloop()

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

    def tamano1(self):
        self.ventana1.geometry("1024x1024")

    def tamano2(self):
        self.ventana1.geometry("1280x1024")

aplicacion1=Aplicacion()