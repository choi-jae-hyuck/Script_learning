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


def put():
    s= input("숫자를 공란으로 분리해서 입력")
    l=s.split()
    l=[eval(i) for i in l]
    result=[]
    for i in l:
        if i not in result:
            result.append(i)
    print(result)
put()