class Rectangle:
    def __init__(self,width=1,height=2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return (self.width+self.height)*2

def test():
    r1=Rectangle(4,10)
    r2=Rectangle(3.5,35.7)
    print("r1 Rectangle width :{0}, height : {1}, Area : {2}, Perimeter : {3}".format(r1.width, r1.width, r1.getArea(),
                                                                                      r1.getPerimeter()))
    print("r1 Rectangle width :{0}, height : {1}, Area : {2}, Perimeter : {3}".format(r2.width, r2.width, r2.getArea(),
                                                                                       r2.getPerimeter()))


class Stock:
    def __init__(self,symbol,name,previous,currnet):
        self.__symbol=symbol
        self.__name=name
        self.__previousPrice=previous
        self.__curentPrice=currnet

    def getSymbol(self):
        return self.__symbol
    def getName(self):
        return self.__name
    def getPreviousPrice(self):
        return self.__previousPrice
    def getCurrentPrice(self):
        return self.__curentPrice

    def setPreviousPrice(self,PreviousPrice):
        self.__previousPrice = PreviousPrice
    def setCurrentPrice(self,currentPrice):
        self.__curentPrice = currentPrice

    def getChangePercent(self):
        return (self.__curentPrice - self.__previousPrice)/self.__curentPrice

    def test():
        s= Stock("INTC","Intel Cor",20500,20350)
        print("가격 변동률 ={0:.2f}%".format(s.getChangePercent()))
    test()

class Fan:
    SLOW=1
    MID=2
    FAST=3
    def __init__(self,speed=SLOW,radius=5,color="Blue",ON=False):
        self.__speed=speed
        self.__ON =ON
        self.__radius =radius
        self.__color=color
    def Print(self):
        print("SPEED : {0} , Radius : {1} , Color : {2} , ON : {3}".format(self.__speed,self.__radius,
                                                                           self.__color,self.__ON))


class Triangle:
    pass


def remove_string():
    file_name=input("File name : ")
    remove_name=input("Remove string : ")
    f=open(file_name)
    S=f.read()
    newS=S.replace(remove_name,"")
    f.close()
    f=open(file_name,'w')
    f.write(newS)
    f.close()

def read_string():
    file_name=input("File name : ")
    f=open(file_name)
    S=f.read()
    character = len(S)
    word= len(S.split())
    line = len(S.split("\n"))
    print("Char : ",character)
    print("Word : ", word)
    print("Line : ", line)
    f.close()

#--------------------------------------------------

from tkinter import *
from tkinter.filedialog import askopenfilename

file_name=""
def fileopen():
    global file_name
    file_name = askopenfilename()
    #e.configure(text=file_name)

def showResult():
    f = open(file_name)
    S = f.read()
    # 알파벳 빈도수
    histogram = [0] * 26
    new = S.lower()
    for c in new:
        if c.isalpha():
            histogram[ord(c) - ord('a')] += 1
    for i in range(26):
        text.insert(END, chr(i + ord('a')) + " = " + str(histogram[i]) + "\n")
    f.close()

window=Tk()
window.title("Alpha")
frame1=Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=Y)
text=Text(frame1,width=50,height=15,wrap=WORD,yscrollcommand=scrollbar.set)
text.pack()
frame2=Frame(window)
frame2.pack()
Label(frame2,text="File name").pack(side=LEFT)
e = Entry(frame2,text="")
e.pack(side=LEFT)
Button(frame2,text="Open",command=fileopen).pack(side=LEFT)
Button(frame2,text="Result",command=showResult).pack(side=LEFT)
window.mainloop()

#--------------------------------------------------------
from tkinter import *
from tkinter.filedialog import askopenfilename

def fileopen():
    file_name = e.get()
    f = open(file_name)
    S = f.read()
    # 알파벳 빈도수
    histogram = [0] * 26
    new = S.lower()
    for c in new:
        if c.isalpha():
            histogram[ord(c) - ord('a')] += 1
    maxCount=max(histogram)
    barW=(600-20)/26
    for i in range(26):
        canvas.create_rectangle(10+i*barW,290-(300*histogram[i]/maxCount)*0.9, 10+(i+1)*barW,300-10)
        canvas.create_text(10 + i * barW + 10, 300 - 5, text=chr(i + ord('a')))
        canvas.create_text(10 + i * barW + 10, 290 - (300 * histogram[i] / maxCount) * 0.9 - 10, text=histogram[i])
    f.close()


window=Tk()
window.title("Alpha")
frame1=Frame(window)
frame1.pack()
canvas = Canvas(frame1, bg="white", width=600, height=300)
canvas.pack()
frame2=Frame(window)
frame2.pack()
Label(frame2,text="Input URL").pack(side=LEFT)
e = Entry(frame2,text="")
e.pack(side=LEFT)
Button(frame2,text="Result",command=fileopen).pack(side=LEFT)
window.mainloop()