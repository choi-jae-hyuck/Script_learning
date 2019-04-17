from tkinter import *
import random
import tkinter.simpledialog
import re

class Card:
    def __init__(self):
        window=Tk()
        frame1=Frame(window)
        frame1.pack()
        Button(frame1,text="Reset",command=self.refresh).pack()

        frame2 = Frame(window)
        frame2.pack()
        self.imageList=[]
        self.index=[x for x in range(52)]
        for i in range(1,52+1):
            self.imageList.append(PhotoImage(file="card/"+str(i)+".gif"))
        self.labelList=[]
        for i in range(4):
            self.labelList.append(Label(frame2,image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3,text="Insert ").pack(side=LEFT)
        self.e=Entry(frame3,text="",width=30)
        self.e.pack(side=LEFT)
        Button(frame3,text="Enter",command=self.verify).pack(side=LEFT)
        window.mainloop()

    def refresh(self):
        random.shuffle(self.index)
        for i in range(4):
            self.labelList[i].configure(image=self.imageList[self.index[i]])

    def verify(self):
        fourCards=[]
        for i in range(4):
            fourCards.append(self.index[i]%13 + 1)
        fourCards.sort()
        expression=self.e.get()
        expression = expression.replace('(',' ')
        expression = expression.replace(')', ' ')
        expression = expression.replace('+', ' ')
        expression = expression.replace('-', ' ')
        expression = expression.replace('*', ' ')
        expression = expression.replace('/', ' ')
        numbers=expression.split()
        numbers=[eval(x) for x in numbers]
        numbers.sort()
        if numbers ==fourCards:
            if eval(self.e.get()) == 24 :
                tkinter.messagebox.showinfo("Correct","Correct")
            else:
                tkinter.messagebox.showinfo("InCorrect",self.e.get()+" is not 24")
        else:
            tkinter.messagebox.showinfo("inCorrect","Use Show Card")


Card()
