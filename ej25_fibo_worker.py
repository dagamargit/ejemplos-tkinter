import tkinter as tk
from time import sleep
import queue
import threading


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()

        self.label1 = tk.Label(text="Introduzca un número:")
        self.label1.grid(column=0, row=0)

        self.dato = tk.StringVar()

        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entry1.grid(column=0, row=1)

        self.boton1 = tk.Button(
            self.ventana1, text="Calcular Fibonacci", command=self.calcularfibo)
        self.boton1.grid(column=0, row=2)

        self.boton2 = tk.Button(
            self.ventana1, text="Calcular Fibonacci Worker", command=self.calcularfibo_worker)
        self.boton2.grid(column=0, row=3)

        self.label2 = tk.Label(text="resultado")
        self.label2.grid(column=0, row=4)
        self.ventana1.mainloop()

    def calcularfibo(self):
        valor = int(self.dato.get())

        self.boton1.config(state="disabled")
        res = self.fibo(valor)
        self.label2.configure(text=res)
        self.boton1.config(state="normal")


    def fibo(self, num):
        if num < 2:
                res = 1
        else:
                fib0 =  1
                fib1 = 1
                for i in range(2,num+1):
                  tmp = fib0 + fib1
                  fib0 = fib1
                  fib1 = tmp
                  sleep(1) # Solo para probar si la interfaz se puede seguir usando

                res = fib1
        return res


    def process_queue(self):
        try:
            res = self.queue.get(0)
            self.label2.configure(text=res)
            self.boton2.config(state="normal")
        except queue.Empty:
            self.ventana1.after(100, self.process_queue)

    def calcularfibo_worker(self):
        valor=int(self.dato.get())
        self.boton2.config(state="disabled")
        self.queue=queue.Queue()    # Para comunicacion con hebra worker
        Worker(self.queue, valor).start()
        self.ventana1.after(100, self.process_queue)


# Hebra trabajadora
class Worker(threading.Thread):
    def __init__(self, queue, num):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num

    def run(self):
        try:
            if self.num<2:
                res = 1
            else:
                fib0 =  1
                fib1 = 1
                for i in range(2,self.num+1):
                  tmp = fib0 + fib1
                  fib0 = fib1
                  fib1 = tmp
                  sleep(1)  # Solo para probar si la interfaz se puede seguir usando

                res = fib1

            self.queue.put(str(fib1))
        except:
            self.queue.put("Error")


aplicacion1=Aplicacion()
