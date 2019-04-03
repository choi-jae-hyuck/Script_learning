from tkinter import *
import random
class Graph:
    def display(self):
        self.canvas.delete("bar")
        lst=[0]*26
        for i in range(1000):
            n=random.randint(0,25)
            lst[n]+=1
        maxCount=int(max(lst))
        self.canvas.create_line(10,300-10,600-10,300-10)
        barw=(600-20)/26
        for i in range(26):
            self.canvas.create_rectangle(10+i*barw,300-(300*lst[i]/maxCount)*0.9, 10+(i+1)*barw,300-10,tags="bar")
            self.canvas.create_text(10+i*barw+10,300-5,text=chr(i+ord('a')),tags="bar")
            self.canvas.create_text(10 + i * barw + 10, 300-(300*lst[i]/maxCount)*0.9 -10, text=lst[i], tags="bar")

    def __init__(self):
        self.window = Tk()
        self.window.title("Graph")
        self.canvas = Canvas(self.window, bg="white", width=600, height=300)
        self.canvas.pack()
        Button(self.window,text="Draw",command=self.display).pack()
        self.frame = Frame(self.window)
        self.frame.pack()
        self.window.mainloop()

Graph()