import tkinter
import random
from tkinter import messagebox
win = tkinter.Tk()

win.geometry("375x150+600+250")
win.resizable(False, False)
win.config(bg='#123456')

lst = ['Yellow','Blue','Green','Red','Orange','White','Purple','Brown']
score = 0

timeleft = 30


def startgame(event):  
    if timeleft == 30:
        countdown()
    nextcolor()


def nextcolor():
    global score
    global timeleft
    if timeleft > 0:
        
        ent.focus_set()
        if ent.get().lower() == lst[1].lower():
            score += 1
        ent.delete(0, tkinter.END)
        random.shuffle(lst)

        label.config(fg = str(lst[1]), text = str(lst[0]))
        scorelabel.config(text = "امتيار: " + str (score))        


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text = "زمان:" + str(timeleft))
        timelabel.after(1000, countdown)
        if timeleft == 0:
            a=messagebox.showerror('time',f'امتیاز کسب شده= {score},  زمان به پایان رسید ')
            win.destroy()




lbl = tkinter.Label(win,bg='#123456',fg='white' ,font='arial 10 bold',text = "رنگ هر کلمه را به زبان انگليسي وارد کنيد")
lbl.pack()

scorelabel = tkinter.Label(win,bg='#123456',fg='white' ,font='arial 10 bold',text = "بزنيد تا بازي شروع شود Enter")
scorelabel.pack()

timelabel = tkinter.Label(win, bg='#123456',fg='white',font='arial 10 bold',text = "زمان:" + str(timeleft) )
timelabel.pack()

label = tkinter.Label(win,bg='#123456',font='arial 20 bold')
label.pack()

ent = tkinter.Entry(win, width = 20)

win.bind('<Return>', startgame)

ent.pack()
ent.focus_set()

win.mainloop()