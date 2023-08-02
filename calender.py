from tkinter import *
from tkcalendar import *


root=Tk()
# root.title('pm.com')
# root.iconbitmap('c:/gui/pm.ico')
root.geometry('600x400')


cal=Calendar(root, selectmode="day", year=2023, month=8, day=2)
cal.pack(pady=20)

def grabDate():
    myLeable.config(text=cal.get_date())




myButton = Button(root, text="Pice Date", command=grabDate)
myButton.pack(pady=20)

myLeable=Label(root,text="")
myLeable.pack(pady=20)



root.mainloop()

