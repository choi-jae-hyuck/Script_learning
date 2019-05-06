from tkinter import *
import random
import tkinter.messagebox
class Linear:
    def __init__(self):
        window=Tk()
        window.title("Research")
        self.i=0
        self.width=600
        self.height=200
        self.canvas=Canvas(window,width=self.width,height=self.height)
        self.canvas.pack()
        frame=Frame(window)
        frame.pack()
        Button(frame,text="Next",command=self.step).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)

        window.mainloop()
    def step(self):
        minIndex=self.i
        for i in range(self.i+1,20):
            if self.numbers[minIndex] > self.numbers[i]:
                minIndex=i
        self.numbers[minIndex],self.numbers[self.i] = self.numbers[self.i] , self.numbers[minIndex]
        self.draw()
        barW = (self.width - 20) / 20
        self.canvas.delete("red")
        self.canvas.create_rectangle(10 + self.i * barW, (1 - self.numbers[self.i] / 21) * (self.height - 10),
                                     10 + (self.i + 1) * barW, self.height,fill='red', tag='red')
        self.i+=1
    def reset(self):
        self.i=0
        self.numbers=[x for x in range(1,21)]
        random.shuffle(self.numbers)
        self.draw()
    def draw(self):
        barW=(self.width-20)/20
        self.canvas.delete("red")
        self.canvas.delete("grim")
        for i in range(20):
            self.canvas.create_rectangle(10+i*barW,(1-self.numbers[i]/21)*(self.height-10),
                                         10+(i+1)*barW, self.height ,tag='grim')
            self.canvas.create_text(25 + i * barW, (1 - self.numbers[i] / 21) * (self.height - 10)-5,
                                         text= str(self.numbers[i]), tag='grim')
Linear()