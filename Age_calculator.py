from tkinter import *
from datetime import datetime

App = Tk()
App.title("Age Calculator")
App.geometry('250x250')
lbl = Label(App, text='Enter your DOB')
lbl.grid(row=0, column=0, columnspan=3)
lbd = Label(App, text='date')
ed = Entry(App, width=2)
lbm = Label(App, text='month')
em = Entry(App, width=2)
lby = Label(App, text='year')
ey = Entry(App, width=4)
lbd.grid(row=1, column=0)
ed.grid(row=1, column=1)
lbm.grid(row=1, column=2)
em.grid(row=1, column=3)
lby.grid(row=1, column=4)
ey.grid(row=1, column=5)


def no_days():
    dat = int(ed.get())
    mon = int(em.get())
    year = int(ey.get())
    dob = datetime(day=dat, month=mon, year=year)
    time_now = datetime.now()
    time_diff = time_now - dob
    msg = Label(App, text='You lived {} days'.format(str(time_diff.days)))
    msg.grid(row=3, column=0, columnspan=4)


def no_seconds():
    dat = int(ed.get())
    mon = int(em.get())
    year = int(ey.get())
    dob = datetime(day=dat, month=mon, year=year)
    time_now = datetime.now()
    time_diff = time_now - dob
    msg = Label(App, text='You lived {} seconds'.format(str(time_diff.total_seconds())))
    msg.grid(row=4, column=0, columnspan=6)


b1 = Button(App, text='Total Days', command=no_days)
b1.grid(row=2, column=0, columnspan=3)
b2 = Button(App, text='Total Seconds', command=no_seconds)
b2.grid(row=2, column=3, columnspan=3)
App.mainloop()
