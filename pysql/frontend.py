"""
A program that stores this information:
Title,Author
Year.ISBN

User can:
View all entries
Select an entry
Update an entry
Delete an entry
Close
"""
from tkinter import *
import backend
def check_for_empty():
    global emptyChecker
    if eTitle=="" and eAuthor=="" and eYear=="" and eISBN=="":
        emptyChecker=FALSE
    else:
        emptyChecker=True

def get_selected_row(event):
    global selected_tuple
    index= lstListView.curselection()
    selected_tuple = lstListView.get(index)
    eTitle.delete(0,END)
    eTitle.insert(END,selected_tuple[1])
    
    eAuthor.delete(0,END)
    eAuthor.insert(END,selected_tuple[2])
    
    eYear.delete(0,END)
    eYear.insert(END,selected_tuple[3])
    
    eISBN.delete(0,END)
    eISBN.insert(END,selected_tuple[4])
    
def view_command():
    lstListView.delete(0,END)
    for row in backend.view():
        lstListView.insert(END,row)# Every new row is put at the end of the row

def search_command():
    lstListView.delete(0,END)
    for row in backend.search(title_txt.get(),author_txt.get(),year_txt.get(),ISBN_txt.get()):
        lstListView.insert(END,row)

def add_command():
    check_for_empty()
    backend.insert(title_txt.get(),author_txt.get(),year_txt.get(),ISBN_txt.get())
    lstListView.delete(0,END)
    lstListView.insert(END,(title_txt.get(),author_txt.get(),year_txt.get(),ISBN_txt.get()))
 
def delete_command():
    backend.delete(selected_tuple[0])
    lstListView.delete(0,END)
    for row in backend.view():
        lstListView.insert(END,row)


def update_command():
    backend.update(selected_tuple[0],eTitle.get(),eAuthor.get(),eYear.get(),eISBN.get())

window = Tk()
lblTitle = Label(window,text = "Title")
lblTitle.grid(row=0,column=0)

lblAuthor = Label(window,text = "Author")
lblAuthor.grid(row=0,column=2)

lblYear = Label(window,text = "Year")
lblYear.grid(row=1,column=0)

lblISBN = Label(window,text = "ISBN")
lblISBN.grid(row=1,column=2)

title_txt = StringVar()
eTitle = Entry(window,textvariable=title_txt)
eTitle.grid(row=0,column=1)

author_txt = StringVar()
eAuthor = Entry(window,textvariable=author_txt)
eAuthor.grid(row=0,column=3)

year_txt = StringVar()
eYear = Entry(window,textvariable=year_txt)
eYear.grid(row=1,column=1)

ISBN_txt = StringVar()
eISBN = Entry(window,textvariable=ISBN_txt)
eISBN.grid(row=1,column=3)

lstListView = Listbox(window,height=6,width=35)
lstListView.grid(row=2,column=0,rowspan=7,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=7)

#tell the scroll bar and the list view of each other's existence
lstListView.configure(yscrollcommand=sb1.set)
sb1.configure(command=lstListView.yview)

#list click event handler
lstListView.bind('<<ListboxSelect>>',get_selected_row)

btnView = Button(window,text="View All ",width = 12,command=view_command)
btnView.grid(row=2,column=3)

btnSrch = Button(window,text="Search Entry ",width = 12,command=search_command)
btnSrch.grid(row=3,column=3)

btnAdd = Button(window,text="Add Entry ",width = 12,command=add_command)
btnAdd.grid(row=4,column=3)

btnUPdate = Button(window,text="Update ",width = 12,command=update_command)
btnUPdate.grid(row=5,column=3)

btnDelete = Button(window,text="Delete ",width = 12,command=delete_command)
btnDelete.grid(row=6,column=3)

btnClose = Button(window,text="Close ",width = 12)
btnClose.grid(row=7,column=3)

window.mainloop()

