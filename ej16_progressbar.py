from tkinter import * 
from tkinter.ttk import *
import time 



class Aplicacion:
    def __init__(self):
        self.ventana = Tk() 

        self.button = Button(self.ventana, text="Comenzar", command=self.bar)
        self.button.pack(pady=10)
        self.progress = Progressbar(self.ventana, orient = HORIZONTAL, 
			length = 100, mode = 'determinate') 
        self.progress.pack(pady=10)
        self.ventana.mainloop()

    def bar(self): 
        for x in range(0,100):
            self.progress['value'] = x
            self.ventana.update_idletasks() 
            time.sleep(0.1) # ¿Podemos interrumpirlo fácilmente?

aplicacion1=Aplicacion() 
