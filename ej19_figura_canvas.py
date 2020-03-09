import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=400, height=400, background="white")
        self.canvas1.pack()

        i=0
        while i<100:
            i+=5
            self.canvas1.create_line([(100,100),(200,100-i),(300,100),(300+i,200),(300,300),(200,300+i),(100,300),(100-i,200),(100,100)], smooth=0) 

        self.ventana1.mainloop()
       

aplicacion1=Aplicacion()