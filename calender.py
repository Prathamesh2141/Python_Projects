from tkinter import *
from tkcalendar import *


root=Tk()
root.title('PMCalender')
# root.iconbitmap('c:/gui/pm.ico')
root.geometry('400x400')


cal=Calendar(root, selectmode="day", date_pattern='dd/mm/yyyy')
cal.pack(pady=20,expand=True,fill='both')

def grabDate():
    myLeable.config(text=cal.get_date())




myButton = Button(root, text="Pice Date", command=grabDate)
myButton.pack(pady=20)

myLeable=Label(root,text="")
myLeable.pack(pady=20)



root.mainloop()

