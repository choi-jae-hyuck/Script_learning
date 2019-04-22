from tkinter import *
import random
class TicTacToe:
    def __init__(self):
        self.window=Tk()
        self.DrawFrame=Frame(self.window)
        self.DrawFrame.pack()
        self.imageList=[]
        self.imageList.append((PhotoImage(file='image/o.gif')))
        self.imageList.append((PhotoImage(file='image/x.gif')))
        self.labelList=[]
        for r in range(3):
            for c in range(3):
                self.labelList.append(Label(self.DrawFrame,image=self.imageList[random.randint(0,1)]))
                self.labelList[r*3+c].grid(row=r,column=c)
        self.ButtonFrame = Frame(self.window)
        self.ButtonFrame.pack()
        Button(self.ButtonFrame,text='Reset',command=self.reset).pack()
        self.window.mainloop()

    def reset(self):
        for r in range(3):
            for c in range(3):
                self.labelList[r*3+c].configure(image=self.imageList[random.randint(0,1)])





TicTacToe()