from tkinter import *
def On_btn_click():
    in_grams = float(e1_value.get())*1000
    t1.delete("1.0",END)
    t1.insert(END,in_grams)
    
    in_pounds = float(e1_value.get())*2.25
    t2.delete("1.0",END)
    t2.insert(END,in_pounds)

    in_ounce = float(e1_value.get())*35.27
    t3.delete("1.0",END)
    t3.insert(END,in_ounce)
#"1.0",END

window = Tk()
b1 = Button(window,text = "Convert",command=On_btn_click)
b1.grid(row=0,column=2)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

lbl1 = Label(window,text="Kilograms")
lbl1.grid(row=0,column=0)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)



window.mainloop()
