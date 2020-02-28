import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.tree = ttk.Treeview(self.ventana1)
        self.tree.grid()

        # https://tkdocs.com/tutorial/tree.html
        self.tree['columns'] = ('size', 'modified', 'owner')

        # self.tree.column('size', width=100, anchor='center')
        self.tree.heading('size', text='Size')
        self.tree.heading('modified', text='Modified')
        self.tree.heading('owner', text='Owner')

        # Treeview chooses the id:
        for x in range(0,20):
            self.tree.insert('', 'end', text='Tutorial'+str(x), values=('primer valor','segundo valor','tercer valor'))

        self.ventana1.mainloop()


aplicacion1=Aplicacion()