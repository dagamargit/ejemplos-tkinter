import tkinter as tk
import random
    
root = tk.Tk()
root.geometry("170x200+30+30") 
     
temas = ['Python','POO','Git','GUI','BBDD']
labels = range(5)
for i in range(5):
   ct = [random.randrange(256) for x in range(3)]
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = tk.Label(root, 
                text=temas[i], 
                bg=bg_colour)
   l.place(x = 20, y = 30 + i*30, width=120, height=25)
          
root.mainloop()