from tkinter import *


class Ball:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.dix = 2
        self.diy = 2

class BallAni:
    def stop(self):
        for i in self.ballList:
            i.dix = 0
            i.diy = 0
    def resume(self):
        for i in self.ballList:
            i.dix = 2
            i.diy = 2
    def add(self):
        self.ballList.append(Ball())
    def remove(self):
        self.ballList.pop()
    def faster(self):
        for i in self.ballList:
            i.dix *= 2
            i.diy *= 2
    def slower(self):
        for i in self.ballList:
            i.dix *= 0.5
            i.diy *= 0.5
    def animate(self):
        while True:
            self.canvas.after(100)
            self.canvas.update()
            self.canvas.delete("Ball")
            for i in self.ballList:
                if i.x>=self.width:
                    i.dix *=-1
                elif i.x<0:
                    i.dix *=-1
                if i.y>=self.height:
                    i.diy *=-1
                elif i.y<0:
                    i.diy *=-1
                i.x+=i.dix
                i.y+=i.diy
                self.canvas.create_oval(i.x-3,i.y-3,i.x+3,i.y+3,fill="red",tags="Ball")

    def __init__(self):
        self.window = Tk()
        self.window.title("Balling")
        self.width=600
        self.height=300
        self.canvas = Canvas(self.window, bg="white", width=self.width, height=self.height)
        self.canvas.pack()
        self.ballList=[]
        self.frame = Frame(self.window)
        self.frame.pack()
        self.S = IntVar
        Button(self.frame, text="Stop", command=self.stop).pack(side=LEFT)
        Button(self.frame, text="Start", command=self.resume).pack(side=LEFT)
        Button(self.frame, text="+", command=self.add).pack(side=LEFT)
        Button(self.frame, text="-", command=self.remove).pack(side=LEFT)
        Button(self.frame, text="Fast", command=self.faster).pack(side=LEFT)
        Button(self.frame, text="Slow", command=self.slower).pack(side=LEFT)
        self.animate()
        self.window.mainloop()

BallAni()