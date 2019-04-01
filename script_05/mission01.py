from tkinter import *
window =Tk()

class Ball:
    def __init__(self,canvas,x,y):
        self.x1=x
        self.x2=x+1
        self.y1=y
        self.y2=y+1

def up():
    canvas.move("Ball", 0, -5)
def left():
    canvas.move("Ball", -5, 0)
def down():
    canvas.move("Ball", 0, 5)
def right():
    canvas.move("Ball", 5, 0)

canvas=Canvas(window,bg="white",width=600,height=300)
canvas.pack()
canvas.create_oval(10,10,20,20,fill="red",tags="Ball")

frame=Frame(window)
frame.pack()
b1=Button(frame,text="W",command=up)
b2=Button(frame,text="A",command=left)
b3=Button(frame,text="S",command=down)
b4=Button(frame,text="D",command=right)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)

window.mainloop()