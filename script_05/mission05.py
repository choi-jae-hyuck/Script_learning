from tkinter import *

class Ball:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.dix = 2
        self.diy = 2

class BallAni:
    def stop(self):
        pass
    def resume(self):
        pass
    def add(self):
        self.ballList.append(Ball())
    def remove(self):
        self.ballList.pop()
    def faster(self):
        pass
    def slower(self):
        pass
    def animate(self):
        while True:
            self.canvas.after(100)
            self.canvas.update()
            self.canvas.delete("Ball")
            for i in self.ballList:
                if Ball.x>=self.width:
                    Ball.dix=-2
                elif Ball.x<0:
                    Ball.dix=2
                if Ball.y>=self.height:
                    Ball.diy=-2
                elif Ball.y<0:
                    Ball.diy=2
                Ball.x+=Ball.dix
                Ball.y+=Ball.diy
                self.canvas.create_oval(Ball.x-3,Ball.y-3,Ball.x+3,Ball.y+3,fill="red",tags="Ball")

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