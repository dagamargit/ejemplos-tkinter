import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.pack()
        self.comprobar_color()

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.pack()

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.pack()

        self.ventana1.mainloop()


    def comprobar_color(self):
        if self.valor>=0:
            self.label1.configure(foreground="blue")
        else:
            self.label1.configure(foreground="red")

    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
        self.comprobar_color()
        # self.label1["text"]=self.valor

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        
        self.comprobar_color()

aplicacion1=Aplicacion()