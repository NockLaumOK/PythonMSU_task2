#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
''' 

from tkinter import *
import random

def dump(*args):
    print("DUMP:",args)

r=1

listColor = ["snow","DarkGreen","green2"] 
def addButton(*args):
    global r
    B1 = Button(root, text = "B")
    B1.grid(row=r,column=0,sticky=W+E)
    L1 = Label(root, text = "L"+str(r), bg="PeachPuff")
    L1.grid(row=r, column=1, sticky=E+W)
    def changeL(event):
        L1.configure(bg='#%02X%02X%02X' % (q(),q(),q()))
    B1.bind('<Button-1>', changeL)
    r=r+1

q = lambda: random.randint(0,255)
print()


TKroot = Tk()
TKroot.title("Task2")
TKroot.geometry('800x480')
TKroot.configure(background = 'black')

root = Frame(TKroot,bg='black')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)
root.grid(sticky=N+E+W)

Butt = Button(root, text="Addффффффффффффффффффф")
Butt.bind('<Button-1>', addButton)
Butt.grid(row=0, column=0, columnspan=1, sticky=S)

Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=0, column=1, columnspan=1, sticky=S)

#Txt = Label(root, text="This is a label", bg="PeachPuff")
#Txt.grid(row=1, column=0, columnspan=2, sticky=E+W)

TKroot.mainloop()
print("Done")
#root.destroy()
