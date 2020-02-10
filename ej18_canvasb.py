import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1)
        self.ventana1.mainloop()

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.ventana1,text="Partidos políticos")
        self.lf1.grid(column=0, row=0, sticky="w")
        self.label1=ttk.Label(self.lf1, text="Partido A:")
        self.label1.grid(column=0,row=0, padx=5, pady=5)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.lf1, text="Partido B:")
        self.label2.grid(column=0,row=1, padx=5, pady=5)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.label3=ttk.Label(self.lf1, text="Partido C:")
        self.label3.grid(column=0,row=2, padx=5, pady=5)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        self.boton1=ttk.Button(self.lf1, text="Generar gráfico", command=self.grafico_barra)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()

    def grafico_barra(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())
        if valor1>valor2 and valor1>valor3:
            mayor=valor1
        else:
            if valor2>valor3:
                mayor=valor2
            else:
                mayor=valor3
        largo1=valor1/mayor*400
        largo2=valor2/mayor*400
        largo3=valor3/mayor*400
        self.canvas1.create_rectangle(10,10,10+largo1,90,fill="red")
        self.canvas1.create_rectangle(10,120,10+largo2,200,fill="blue")
        self.canvas1.create_rectangle(10,230,10+largo3,310,fill="green")
        self.canvas1.create_text(largo1+70, 50, text="partido A", fill="white", font="Arial")
        self.canvas1.create_text(largo2+70, 160, text="partido B", fill="white", font="Arial")
        self.canvas1.create_text(largo3+70, 270, text="partido C", fill="white", font="Arial")
        

aplicacion1=Aplicacion()