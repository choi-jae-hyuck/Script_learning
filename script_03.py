import random
def card():
    num=random.randint(0,12)
    pattern=random.randint(0,3)
    a=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    b=["Clover","Diamond","Heart","Spad"]
    print("Card is {0} {1}".format(b[pattern],a[num]))


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
        print(startPeg,"번 기둥의", ndisks, "번 원반을", endPeg,"번 기둥에 옮김니다.")
        count+=1
        hanoi(ndisks-1,6-startPeg-endPeg, endPeg)
    print("All movement ="count)

def tobinary():
    value = eval(input("INPUT NUM :"))
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
