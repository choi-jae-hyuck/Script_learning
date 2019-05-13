from tkinter import *
import random
import tkinter.messagebox
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
        self.endgame=False
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
        if self.buttonList[r * 3 + c]['text'] == ' ' and self.endgame is False:
            if self.turn :
                self.buttonList[r * 3 + c].configure(image=self.imageList[0])
                self.buttonList[r * 3 + c].configure(text='O')
            else:
                self.buttonList[r * 3 + c].configure(image=self.imageList[1])
                self.buttonList[r * 3 + c].configure(text='X')
            self.turn=not self.turn
            if self.turn is True and self.endgame is False:
                self.explain.configure(text="Turn O")
            elif self.turn is False and self.endgame is False:
                self.explain.configure(text="Turn X")
        self.check_row()
        self.check_col()
        self.check_diagoDown()
        self.check_diagoUp()
        if self.endgame is True:
            tkinter.messagebox.showinfo("End","End Game")
    def check_row(self):
        if self.endgame is False:
            for r in range(3):
                for c in range(1):
                    if self.buttonList[r*3 +c+0]['text'] is self.buttonList[r*3 +c+1]['text']\
                            and self.buttonList[r*3 +c+0]['text'] is self.buttonList[r*3 +c+2]['text'] :
                        if self.buttonList[r*3 +c+0]['text'] is 'O':
                            print(1)
                            self.endgame = True
                        elif self.buttonList[r*3 +c+0]['text'] is 'X':
                            print(1)
                            self.endgame = True

    def check_col(self):
        if self.endgame is False:
            for r in range(1):
                for c in range(3):
                    if self.buttonList[r + 0 + c ]['text'] is self.buttonList[r + 3 + c ]['text'] \
                            and self.buttonList[r + 0 + c ]['text'] is self.buttonList[r +6 + c ]['text']:
                        if self.buttonList[r + 0 + c ]['text'] is 'O':
                            print(1)
                            self.endgame = True
                        elif self.buttonList[r + 0 + c ]['text'] is 'X':
                            print(1)
                            self.endgame = True
    def check_diagoDown(self):
        if self.endgame is False:
            for r in range(1):
                for c in range(1):
                    if self.buttonList[r * 3 + c + 0]['text'] is self.buttonList[r * 3 + c + 1 +3]['text'] \
                            and self.buttonList[r * 3 + c + 0]['text'] is self.buttonList[r * 3 + c + 2 +6]['text']:
                        if self.buttonList[r * 3 + c + 0]['text'] is 'O':
                            print(1)
                            self.endgame = True
                        elif self.buttonList[r * 3 + c + 0]['text'] is 'X':
                            print(1)
                            self.endgame = True
    def check_diagoUp(self):
        if self.endgame is False:
            for r in range(1):
                for c in range(1):
                    if self.buttonList[r * 3+2 + c + 0]['text'] is self.buttonList[r * 3+2 + c + 2]['text'] \
                            and self.buttonList[r * 3+2 + c + 0]['text'] is self.buttonList[r * 3+2 + c + 4]['text']:
                        if self.buttonList[r * 3+2 + c + 0]['text'] is 'O':
                            print(1)
                            self.endgame = True
                        elif self.buttonList[r * 3+2 + c + 0]['text'] is 'X':
                            print(1)
                            self.endgame = True
TicTacToe()