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
    x1=math.radians(x1)
    x2=math.radians(x2)
    x3=math.radians(x3)
    x4=math.radians(x4)
    y1=math.radians(y1)
    y2=math.radians(y2)
    y3=math.radians(y3)
    y4=math.radians(y4)
    r=6371.01
    s1=r*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    s2=r*math.acos(math.sin(x2)*math.sin(x3)+math.cos(x2)*math.cos(x3)*math.cos(y2-y3))
    s3=r*math.acos(math.sin(x3)*math.sin(x4)+math.cos(x3)*math.cos(x4)*math.cos(y3-y4))
    s4=r*math.acos(math.sin(x4)*math.sin(x1)+math.cos(x4)*math.cos(x1)*math.cos(y4-y1))
    S1=(s1+s2+s3)/2
    S2=(s2+s3+s4)/2
    area=(S1*(S1-s1)*(S1-s2)*(S1-s3))**0.5+(S2*(S2-s2)*(S2-s3)*(S2-s4))**0.5
    area=int(area*10)/10
    print("Area is ",area,"Km")

import math
def satle():?
    x1,y1=eval(input("input first(x,y) : "))
    x2,y2=eval(input("input second(x,y) : "))
    x1=math.radians(x1)
    x2=math.radians(x2)
    y1=math.radians(y1)
    y2=math.radians(y2)
    r=6371.01
    d=r*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    print(d)

def asc():
    word=eval(input("ASCII CODE: "))
    print("Word is ",chr(word))

import time
def timer():
    word=int(time.time()%26)+ord('A')
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

def average():
    lis=input("INPUT SCORE : ")
    lis=lis.split()
    lis=[eval(i) for i in lis]
    up,down=[],[]
    Sum=0
    account=0
    for i in lis:
        Sum+=i
        account+=1
    average=Sum/account
    for i in lis:
        if i<average : down.append(i)
        elif i>average : up.append(i)
    print("Average : ",average)
    print("Average UP : ",up)
    print("Average Down : ",down)

def origin():
    lis=input("INPUT SCORE : ")
    lis=lis.split()
    lis=[eval(i) for i in lis]
    original = list(set(lis))
    print(original)

def lst(lis):
    count = 0
    for i in lis:
        count+=1
    print("List count : ",count,", List first index : ",lis[0],", List Last index : ",lis[count-1])
    print("List[2] : ",lis[2],", List[-2] : ",lis[-2])

def small(lst):
    lst.sort()
    print("Minimum : ",lst[0])

def sorting(lst):
    a=lst[0]
    sort=True
    for i in lst:
        if a<=i and sort is True:
            a=i
        elif a>i:
            sort=False
    if sort is True:
        print("List is sorting")
    else :
        print("List is not sorting")

import random
def bean():
    beans=eval(input("Bean : "))
    num=eval(input("Slot : "))
    slot=[0 for i in range(0,num)]
    bean=["" for i in range(0,beans)]
    for i in range(0,beans):
        move=0
        for j in range(0,num):
            LR=random.randrange(1,2+1)
            if LR is 1:
                bean[i]+=str("L")
            elif LR is 2:
                bean[i]+=str("R")
                move+=1
        slot[move]+=1
    for i in range(0,beans):
        print(bean[i])
    hang=max(slot)
    show=[""for i in range(0,hang+1)]
    for i in range(max(slot),0-1,-1):
        for j in range(0,num):
            if slot[j]>0:
                show[i]+=str("0")
                slot[j]-=1
            elif slot[j] is 0 :
                show[i]+=str(" ")
    for i in range(0,hang+1):
        print(show[i])

def sumcolum(m,colum):
    lis=['' for i in range(0,m)]
    for i in range(0,m):
        x=print(m,"x",colum,"'s ",i,"line inputs :",)
        lis[i]=input()
        lis[i]=lis[i].split()
        lis[i]=list(map(float,lis[i]))
    for i in range(0,m):
        print(i,"'s Sum : ",sum(lis[i]))

def findmore():
    lis=input("Input index : ")
    lis=lis.split()
    count ={}
    for i in lis:
        try : count[i]+=1
        except: count[i]=1
    key_max=max(count.values())
    for i,j in count.items():
        if key_max is j:
            print("Most : ",i)

def sortcol(m):
    col=[0 for i in range(0,m)]
    print("INPUT ",m,"x",m)
    for i in range(0,m):
        col[i]=input()
        col[i]=col[i].split()
        col[i]=list(map(float,col[i]))
    for i in range(0,m):
        for j in range(0,m):
            if j>i:
                col[i][j],col[j][i]=col[j][i],col[i][j]
    for i in range(0,m):
        col[i].sort()
    for i in range(0,m):
        for j in range(0,m):
            if j>i:
                col[i][j],col[j][i]=col[j][i],col[i][j]
    for i in range(0,m):
        print(col[i])

def RD():
    lis=input("6 Point(x,y) : ")
    lis=lis.split()
    lis=list(map(float,lis))
    num=0
    rd=[]
    for i in range(0,12,2):
        if lis[i]>0 and lis[i+1]<0:
            rd.append([lis[i],lis[i+1]])
            num+=1
    length=0
    print(num)
    for i in range(0,num):
        if length>rd[i][0]**2+rd[i][1]**2:
            pass
        else:
            length=rd[i][0]**2+rd[i][1]**2
            x=rd[i][0]
            y=rd[i][1]
    print("East South : ",x,",",y)
        
