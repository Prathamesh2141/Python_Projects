
from tkinter import *
from tkcalendar import Calendar

# Creat tkinter

cal = Tk()

#The geomentry

cal.geometry("400x400")
cal.title("Calendar picker")

#creat calender object

tkc = Calendar(cal,selectmode = "day",year=2022,date=5,month=9)

#display win

tkc.pack(pady=40)

#date 

def fetch_date():
    date.config(text = "selected date is : " + tkc.get_date())

#add button

butn = Button(cal,text="Select Date",command=fetch_date, bg="white")



butn.pack()

#Label for showing date 

date = Label(cal,bg='white')

date.pack(pady=20)

#star the obj

cal.mainloop()