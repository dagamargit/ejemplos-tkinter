import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.bind("<Motion>", self.mover_mouse)
        self.canvas1.bind("<Button-1>", self.presion_mouse)

        # self.canvas1.bind("<Shift Button-1>", self.presion_mouse) presionar shift+boton izquierdo
        # Button-2 central, Button-3 derecho
        # self.canvas1.bind("<Enter>", self.entrada)
        # self.canvas1.bind("<Leave>", self.salida)
        # self.canvas1.bind("<Double-Button-1>", self.presion_mouse)

        self.canvas1.grid(column=0, row=1)
        self.ventana1.mainloop()

    def presion_mouse(self, evento):
        self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5, fill="red")

    def mover_mouse(self, evento):        
        self.ventana1.title(str(evento.x)+"-"+str(evento.y))

aplicacion1=Aplicacion()