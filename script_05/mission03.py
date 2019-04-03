from tkinter import *
class Radio:
    def display(self):
        self.canvas.delete("Rect")
        if self.v.get()==1:
            if self.fill.get() == 1:
                self.canvas.create_rectangle(300 - 200, 150 - 100, 300 + 200, 150 + 100, fill="red", tags="Rect")
            else:
                self.canvas.create_rectangle(300 - 200, 150 - 100, 300 + 200, 150 + 100, fill="white", tags="Rect")
        elif self.v.get()==2:
            if self.fill.get() == 1:
                self.canvas.create_oval(300 - 200, 150 - 100, 300 + 200, 150 + 100, fill="red", tags="Ball")
            else:
                self.canvas.create_oval(300 - 200, 150 - 100, 300 + 200, 150 + 100, fill="white", tags="Ball")
    def __init__(self):
        self.window = Tk()
        self.window.title("Radio Check")
        self.canvas = Canvas(self.window,bg="white",width=600,height=300)
        self.canvas.pack()
        self.frame = Frame(self.window)
        self.frame.pack()
        self.v=IntVar()
        self.R1=Radiobutton(self.frame,text="Rectangle",variable=self.v,value=1,command=self.display).pack(side=LEFT)
        self.R2 = Radiobutton(self.frame, text="Ball", variable=self.v, value=2, command=self.display).pack(side=LEFT)
        self.fill=IntVar()
        Checkbutton(self.frame,text="Fill",variable=self.fill,command=self.display).pack(side=LEFT)
        self.window.mainloop()


Radio()