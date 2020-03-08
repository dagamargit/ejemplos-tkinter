import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=900, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        archi1=tk.PhotoImage(file="img/carta1.png")
        self.canvas1.create_image(30, 100, image=archi1, anchor="nw", tags="movil")
        archi2=tk.PhotoImage(file="img/carta2.png")
        self.canvas1.create_image(400, 100, image=archi2, anchor="nw", tags="movil")
        self.canvas1.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)  # solamente para las figuras con tag movil
        self.canvas1.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.carta_seleccionada = None
        self.ventana1.mainloop()

    def presion_boton(self, evento):
        carta = self.canvas1.find_withtag(tk.CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.canvas1.move(carta, x - x1, y - y1)
        self.carta_seleccionada = (carta, x, y)    

aplicacion1=Aplicacion()