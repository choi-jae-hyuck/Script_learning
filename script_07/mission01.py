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
        self.imageList.append((PhotoImage(file='image/empty.gif')))
        self.buttonList=[]
        self.turn=True
        for r in range(6):
            for c in range(7):
                self.buttonList.append(\
                    Button(self.DrawFrame,text=' ',image=self.imageList[2],command=lambda Row=r, Col=c: self.press(Row,Col)))
                self.buttonList[r*7+c].grid(row=r,column=c)
        self.ButtonFrame = Frame(self.window)
        self.ButtonFrame.pack()
        Button(self.ButtonFrame, text='Reset', command=self.reset).pack()
        self.window.mainloop()

    def reset(self):
        for r in range(6):
            for c in range(7):
                self.buttonList[r * 7 + c].configure(image=self.imageList[2])
                self.buttonList[r * 7 + c].configure(text=' ')

    def press(self,r,c):
        for i in range(5,-1,-1): # 5 4 3 2 1 0
            if self.buttonList[i*7+c]['text'] == ' ':
                if self.turn:
                    self.buttonList[i * 7 + c].configure(image=self.imageList[0])
                    self.buttonList[i * 7 + c].configure(text='O')
                else:
                    self.buttonList[i * 7 + c].configure(image=self.imageList[1])
                    self.buttonList[i * 7 + c].configure(text='X')
                self.turn = not self.turn
                break

    def check(self):
        pass

TicTacToe()