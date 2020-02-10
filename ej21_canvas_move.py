import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.cuadrado=self.canvas1.create_rectangle(150,10,200,60, fill="red")
        self.ventana1.bind("<KeyPress>", self.presion_tecla)
        self.ventana1.mainloop()
       
    def presion_tecla(self, evento):
        if evento.keysym=='Right':
            self.canvas1.move(self.cuadrado, 4, 0)
        if evento.keysym=='Left':
            self.canvas1.move(self.cuadrado, -4, 0)
        if evento.keysym=='Down':
            self.canvas1.move(self.cuadrado, 0, 4)
        if evento.keysym=='Up':
            self.canvas1.move(self.cuadrado, 0, -4)


aplicacion1=Aplicacion()