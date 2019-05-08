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
        for r in range(3):
            for c in range(3):
                self.buttonList.append(\
                    Button(self.DrawFrame,text=' ',image=self.imageList[2],command=lambda Row=r, Col=c: self.press(Row,Col)))
                self.buttonList[r*3+c].grid(row=r,column=c)
        self.ShowFrame = Frame(self.window)
        self.ShowFrame.pack()
        self.explain=Label(self.ShowFrame,text="Turn O")
        self.explain.pack()
        self.window.mainloop()

    def press(self,r,c):
        if self.buttonList[r * 3 + c]['text'] == ' ':
            if self.turn :
                self.buttonList[r * 3 + c].configure(image=self.imageList[0])
                self.buttonList[r * 3 + c].configure(text='O')
            else:
                self.buttonList[r * 3 + c].configure(image=self.imageList[1])
                self.buttonList[r * 3 + c].configure(text='X')
            self.turn=not self.turn

    def check_row(self):
        for r in range(3):
            for c in range(1):
                if self.buttonList[r*3 +c+0]['text'] is self.buttonList[r*3 +c+1]['text']\
                    and self.buttonList[r*3 +c+0]['text'] is self.buttonList[r*3 +c+2]['text'] :
                    pass

        pass

TicTacToe()