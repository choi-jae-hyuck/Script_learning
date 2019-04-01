from tkinter import *
window =Tk()

radio1=IntVar()
radio2=IntVar()

r1=Radiobutton(window,text="1",value=3,variable=radio1)
r2=Radiobutton(window,text="2",value=3,variable=radio1)
r1.pack()
r2.pack()

window.mainloop()