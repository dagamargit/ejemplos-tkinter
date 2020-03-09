import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.fig = Figure()
    
        self.ax = self.fig.add_subplot(111) # https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.subplot.html: nºfilas, nºcolumnas, índice subplotcd
        self.ax.set_xlabel("X axis")
        self.ax.set_ylabel("Y axis")
        self.ax.cla()   # clear axis
        self.ax.grid()  # configura grid
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(0, 100)

        x = range(-10,11)
        y = [v*v for v in x]
        self.line, = self.ax.plot(x, y, marker='o', color='orange')

        self.graph = FigureCanvasTkAgg(self.fig, master=self.ventana)   # Agg: Anti-Grain geometry rendering engine
        self.graph.get_tk_widget().pack(side="top",fill='both',expand=True)        

        self.ventana.mainloop()

Aplicacion()