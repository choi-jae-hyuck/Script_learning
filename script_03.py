def equation():
    lst=eval(input("Input A b c :"))
    a=lst[0]
    b=lst[1]
    c=lst[2]
    judge=(b**2)-(4*a*c)
    r1= (-b+((b**2)-4*a*c)**0.5) / (2*a)
    r2= (-b-((b**2)-4*a*c)**0.5) / (2*a)

    if judge < 0:
        print("No real root")
    elif judge > 0:
        print("Real root is {0:.6f} , {1:.5f}".format(r1,r2))
    else:
        print("Real root is {0:.6f}".format(r1))

import random
def card():
    num=random.randint(0,12)
    pattern=random.randint(0,3)
    a=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    b=["Clover","Diamond","Heart","Spad"]
    print("Card is {0} {1}".format(b[pattern],a[num]))

def triangle():
    lst=eval(input("Input (x,y) : "))
    x=lst[0]
    y=lst[1]

    if y>100-(0.5*x) and x>0 and y>0:
        print("Point is out of triangle")
    else:
        print("Point in triangle")


def comission():
    goal=25000000
    sales=1
    comission=0
    while comission<goal:
        if sales>10000000:
            comission= 500000*0.08 + 5000000*0.1 + (sales-10000000)*0.12
        elif sales>5000000:
            comission= 500000*0.08 + (sales-5000000)*0.1
        else:
            comission= sales*0.08
        sales +=1
    print("Sales= ",sales)

def monte():
    number=[0]*4
    for i in range(1000000):
        x=random.random() * 2 - 1
        y=random.random() * 2 - 1
        if x<0 :
            number[0] += 1
        elif y< 0:
            number[3] += 1
        elif x>=0 and x<=1 and y>=0 and y<=1:
            y1= -x+1
            if y1 >=y:
                number[2] +=1
            else:
                number[1] +=1
    print(number)
    print((number[0]+number[2])/1000000)

def reverse(number):
    num=str(number)
    num=int(num[::-1])
    return num

def ispal(number):
    num1=number
    num2=reverse(number)
    if num1 == num2:
        return True
    else:
        return False

def display():
    lst=eval(input("Input 3 Number :"))
    lst=[i for i in lst]
    lst.sort()
    print("Sorting : {0}, {1}, {2}".format(lst[0],lst[1],lst[2]))

def printChar(ch1,ch2,number):
    num1=ord(ch1)
    num2=ord(ch2)
    prt=str()
    for i in range(0,number):
        prt+=chr(num1)
        if num1<num2:
            num1+=1
    print(prt)
    

def m1(i):
    print("i      m(i)")
    l=0
    for i in range(1,i+1):
        l+=i/(i+1)
        print("{0}      {1:.4f}".format(i,l))

def gcd(m,n):
    if m%n is 0:
        print("gcd(",m ,",", n,") =", n)
    else :
        gcd(n,m%n)

def m2(i):
    if i is 1:
        return 1
    else :
        return 1/i+m2(i-1)
    
count =0
def hanoi(ndisks,startPeg=1, endPeg=3):
    global count
    if ndisks:
        hanoi(ndisks-1,startPeg,6-startPeg-endPeg)
        count+=1
        hanoi(ndisks-1,6-startPeg-endPeg, endPeg)
print("All Hanoi movement =",count)

def binary():
    value = eval(input("INPUT NUM :"))
    print(tobinary(value))

def tobinary(value):
    if value is 0:
        return ""
    return tobinary(value//2)+str(value%2)

def tohex():
    value = eval(input("INPUT NUM :"))
    if value is 0:
        temp= ""
    elif value%16 is 11:
        temp= "A"
    elif value%16 is 12:
        temp= "B"
    elif value%16 is 13:
        temp= "C"
    elif value%16 is 14:
        temp= "D"
    elif value%16 is 15:
        temp= "F"
    else :
        temp =str(value%16)
    return tobinary(value//16)+temp
