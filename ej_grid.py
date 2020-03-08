from tkinter import Tk, Label, RAISED

root = Tk()
labels = [['1', '2', '3'],     
          ['4', '5', '6'],     
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):
    for c in range(3):
        # crear label para fila r y columna c
        label = Label(root,
                      relief=RAISED,      
                      padx=10,            
                      text=labels[r][c])
        # colocar  label en fila r y columna c
        label.grid(row=r, column=c)

root.mainloop()
