from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE
root = Tk()

text = Label(root,                                              
             font=('Helvetica', 16, 'bold italic'),           
             foreground='white',   
             background='black', 
             pady=10,  
             text='Universidad de Málaga')
text.pack(side=BOTTOM)

uma1 = PhotoImage(file='img/uma1.png')
umaLabel = Label(root,
                   borderwidth=3,  
                   relief=RIDGE,   
                   image=uma1)
umaLabel.pack(side=LEFT)

uma2 = PhotoImage(file='img/uma2.png')
uma2Label = Label(root,
                    image=uma2)
uma2Label.pack(side=RIGHT)

root.mainloop()
