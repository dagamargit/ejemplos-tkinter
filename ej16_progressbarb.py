from tkinter import * 
from tkinter.ttk import *
import time 
import threading
import queue

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
        self.button.configure(state=DISABLED)
        self.queue=queue.Queue()
        ThreadedTask(self.queue).start()
        self.ventana.after(100, self.process_queue)


    def process_queue(self):
        try:
            msg = self.queue.get(0)
            self.progress['value'] = int(msg)
            if int(msg)<100:
                self.ventana.after(100, self.process_queue)
            else:
                self.button.configure(state="normal")

        except queue.Empty:
            self.ventana.after(100, self.process_queue)



class ThreadedTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        try:
            for x in range(0,101):
                print('Poniendo '+str(x))
                self.queue.put(str(x))
                time.sleep(0.1)
        except:
            self.queue.put("Error")


aplicacion1=Aplicacion() 
