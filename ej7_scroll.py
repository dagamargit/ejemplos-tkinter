import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0,row=0)

        self.scroll1.configure(command=self.listbox1.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')    # NS de norte a sur

        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.listbox1.insert(6,"limon")
        self.listbox1.insert(7,"kiwi")
        self.listbox1.insert(5,"banana")
        self.listbox1.insert(5,"uva")
        self.listbox1.insert(5,"papaya")
        self.listbox1.insert(5,"mandarina")
        self.listbox1.insert(5,"frutilla")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(text="Seleccionado:")
        self.label1.grid(column=0, row=2)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion1=Aplicacion()