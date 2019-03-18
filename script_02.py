def times(a=10,b=20):
    return a*b

def swap(x,y):
    return y,x

def intersection(prelist,postlist):
    retlist=[]
    for x in prelist:
        if x in postlist and x not in retlist:
            retlist.append(x)
    return retlist

def chag(x):
    x=x[:]
    x[0]='H'
    return x

def connetURL(server,port):
    str="http://"+server+":"+port
    return str

def hanoi(ndisks,startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1,startPeg,6-startPeg-endPeg)
        print(startPeg,"번 기둥의", ndisks, "번 원반을", endPeg,"번 기둥에 옮김니다.")
        hanoi(ndisks-1,6-startPeg-endPeg, endPeg)

===============================================
def triangles():
    x1,y1,x2,y2,x3,y3=eval(input("input Length : "))
    s1=((x1-x2)**2+(y1-y2)**2)**0.5
    s2=((x2-x3)**2+(y2-y3)**2)**0.5
    s3=((x3-x1)**2+(y3-y1)**2)**0.5
    S=(s1+s2+s3)/2
    area=(S*(S-s1)*(S-s2)*(S-s3))**0.5
    area=int(area*10)/10
    print("Area is ",area)

def quads():
    x1,y1,x2,y2,x3,y3,x4,y4=eval(input("input Length : "))
    s1=((x1-x2)**2+(y1-y2)**2)**0.5
    s2=((x2-x3)**2+(y2-y3)**2)**0.5
    s3=((x3-x4)**2+(y3-y4)**2)**0.5
    s4=((x4-x1)**2+(y4-y1)**2)**0.5
    S1=(s1+s2+s3)/2
    S2=(s2+s3+s4)/2
    area=(S1*(S1-s1)*(S1-s2)*(S1-s3))**0.5+(S2*(S2-s2)*(S2-s3)*(S2-s4))**0.5
    area=int(area*10)/10
    print("Area is ",area)

import math
def satle():?
    x1,y1=eval(input("input first(x,y) : "))
    x2,y2=eval(input("input second(x,y) : "))
    x1=math.radians(x1)
    x2=math.radians(x2)
    y1=math.radians(y1)
    y2=math.radians(y2)
    r=6370.01
    d=r*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    print(d)

def asc():
    word=eval(input("ASCII CODE: "))
    print("Word is ",chr(word))

import time
def timer():
    word=int(time.time()%26+65)
    print(chr(word))

def money():
    name=input("Name : ")
    time=eval(input("Hour per Week : "))
    pay=eval(input("Pay per Hour : "))
    tax=eval(input("Tax : "))
    region=eval(input("Region Tax : "))
    allpay=pay*time
    
    print("\nName = ",name)
    print("Pay = ",pay)
    print("All Pay = ",allpay)
    print("Deduction")
    print("  Tax (",tax*100,"%) : ",allpay*tax)
    print("  Region Tax (",region*100,"%) : ",int(allpay*region))
    print("  All Tax : ",int(allpay*(tax+region)))
    print("  salary : ",int(allpay-allpay*(tax+region)))
    
def reversing():
    lis=input("LIST : ")
    lis=lis.split()
    lis.reverse()
    print(lis)

def iner():
    lis=input("LIST : ")
    lis=lis.split()
    lis.sort()
    dic={}
    for i in lis:
        dic[i]=0
    for i in lis:
        dic[i]=dic[i]+1
    for i in dic.keys():
        print(i," =",dic[i],"piece")
