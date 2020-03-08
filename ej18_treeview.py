import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(self.ventana1, yscrollcommand=self.scroll1.set)
        self.tree.grid()
        
        self.scroll1.configure(command=self.tree.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')    # NS de norte a sur


        # https://tkdocs.com/tutorial/tree.html
        self.tree['columns'] = ('size', 'modified', 'owner')

        # self.tree.column('size', width=100, anchor='center')
        self.tree.heading('#0', text='Name')
        self.tree.heading('size', text='Size')
        self.tree.heading('modified', text='Modified')
        self.tree.heading('owner', text='Owner')

        # Treeview chooses the id:
        for x in range(0,20):
            self.tree.insert('', 'end', text='Tutorial'+str(x), values=('primer valor','segundo valor','tercer valor'))

        self.ventana1.mainloop()


aplicacion1=Aplicacion()