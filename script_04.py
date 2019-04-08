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