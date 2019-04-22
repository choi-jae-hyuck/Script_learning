from tkinter import *
import random
class TicTacToe:
    def __init__(self):
        window=Tk()
        imageList=[]
        imageList.append((PhotoImage(file='image/o.gif')))
        imageList.append((PhotoImage(file='image/x.gif')))
        for r in range(3):
            for c in range(3):
                Label(window,image=imageList[random.randint(0,1)]).grid(row=r,column=c)
        window.mainloop()

TicTacToe()