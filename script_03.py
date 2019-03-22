import random
def monte():
    num=0
    for i in range(0,1000000):
        t=random.randrange(1,100+1)
        if t<76:
            num+=1
    print("Dart Percent : ",num/1000000,"%")

def reverse(number):
    num=str(number)
    print(num[::-1])

def gcd(m,n):
    if m%n is 0:
        print("gcd(",m ,",", n,") =", n)
    else :
        gcd(n,m%n)

def m(i):
    if i is 1:
        return 1
    else :
        return 1/i+m(i-1)
    
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
