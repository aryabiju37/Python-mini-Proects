from tkinter import *

def On_btn_click():
    miles = float(e1_value.get())*0.60
    t1.insert(END,miles)

window = Tk()
b1= Button(window,text="Execute",command=On_btn_click)
#where to put the button
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()
