from tkinter import *
window =Tk()
def program():
    money=float(e1.get())
    year=int(e2.get())
    per=float(e3.get())
    DON=money * ((1+per)**(year*12))
    e4 = Label(window, text=DON)
    e4.grid(row=3, column=1)
l1=Label(window,text="투자금")
l2=Label(window,text="기간")
l3=Label(window,text="월이율")
l4=Label(window,text="미래가치")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
b1=Button(window,text="계산하기",command=program)
b1.grid(row=4,column=1,sticky=E)
window.mainloop()
