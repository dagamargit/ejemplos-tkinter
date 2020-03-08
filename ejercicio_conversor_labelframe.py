import tkinter as tk
import tkinter.ttk as ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Conversor de Temperaturas")

        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Datos de Entrada:")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        

        self.label1=tk.Label(self.labelframe1, text="Cantidad:")
        self.label1.grid(column=0, row=0)
        
        self.dato=tk.StringVar(value="0.0")        
        self.entryCantidad=tk.Entry(self.labelframe1, width=10, textvariable=self.dato)
        self.entryCantidad.grid(column=1, row=0)

        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        
        self.radio1=tk.Radiobutton(self.labelframe1,text="Kelvin", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.labelframe1,text="Celsius", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.labelframe1,text="Fahrenheit", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=1)


        self.labelframe2=ttk.LabelFrame(self.ventana1, text="Datos Conversión:")        
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)        

        self.boton1=tk.Button(self.labelframe2, text="Convertir a:", command=self.convertir)
        self.boton1.grid(column=1, row=2)

        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.labelframe2,text="Kelvin", variable=self.seleccion1)
        self.check1.grid(column=0, row=3)

        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.labelframe2,text="Celsius", variable=self.seleccion2)
        self.check2.grid(column=1, row=3)

        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.labelframe2,text="Fahrenheit", variable=self.seleccion3)
        self.check3.grid(column=2, row=3)

        self.labelframe3=ttk.LabelFrame(self.ventana1, text="Resultados:")        
        self.labelframe3.grid(column=0, row=2, padx=5, pady=10, sticky="WE")        

        self.labelResKelvin1=tk.Label(self.labelframe3, text="Kelvin:")
        self.labelResKelvin1.grid(column=0, row=4)

        self.labelResKelvin2=tk.Label(self.labelframe3, )
        self.labelResKelvin2.grid(column=1, row=4)

        self.labelResCelsius1=tk.Label(self.labelframe3, text="Celsius:")
        self.labelResCelsius1.grid(column=0, row=5)

        self.labelResCelsius2=tk.Label(self.labelframe3, )
        self.labelResCelsius2.grid(column=1, row=5)

        self.labelResFahrenheit1=tk.Label(self.labelframe3, text="Fahrenheit:")
        self.labelResFahrenheit1.grid(column=0, row=6)

        self.labelResFahrenheit2=tk.Label(self.labelframe3, )
        self.labelResFahrenheit2.grid(column=1, row=6)

        self.ventana1.mainloop()

    def convertir(self):
        if self.seleccion.get()==1:
            self.convertir_desde_kelvin()        
        pass        

    def convertir_desde_kelvin(self):        
        if self.seleccion1.get()==1:
            self.labelResKelvin2.configure(text=self.dato.get(), foreground="blue")
        else:
            self.labelResKelvin2.configure(text="-", foreground="red")

        if self.seleccion2.get()==1:    # kelvin a celsius
            self.labelResCelsius2.configure(text=float(self.dato.get())-273.15, foreground="blue")
        else:
            self.labelResCelsius2.configure(text="-", foreground="red")

        if self.seleccion3.get()==1:    # kelvin a fahrenheit
            self.labelResFahrenheit2.configure(text=float(self.dato.get())*9/5-459.67, foreground="blue")
        else:
            self.labelResFahrenheit2.configure(text="-", foreground="red")


aplicacion1=Aplicacion()