def width(a,b):
    print("(폭 X 높이) = 넓이")
    print(a ,"x",b,"=",a*b)
    print("둘레 = ",(a+b)*2)

def spid(x,y):
    mile = 1/1.6
    h=y/60
    print(x,"Km =", x*mile,"Mile")
    print("평균속력 = ",x*mile/h,"mph")

def pop(now):
    year=365*24*60*60
    birth=year//7
    death=year//13
    imm=year//45
    print("now = ",now)
    for i in [1,2,3,4,5]:
        print(i*5,"year = ",now+(birth-death+imm)*i*5)

def found():
    fou= eval(input("found ? = "))
    kilo=fou * 0.454
    print(fou,"found = ", kilo,"kilogram")

def tip():
    subtotal,rate=eval(input("subtotal ? = , rate ? = "))
    tip=subtotal * rate/100
    total=subtotal+tip
    tip=int(tip*100)/100
    total=int(total*100)/100
    print("Tip = ",tip," All price = ",total)

def allsum():
    num=eval(input("0~1000 insert : "))
    sum=0
    while num>0:
        sum += num%10
        num=num//10
    print("Allsum : ",sum)

def cal():
    minute=eval(input("Minute : "))
    day=minute //(24*60)
    year = day//365
    day=day%365
    print(year,"Year ",day,"Days")

def hit():
    goal=eval(input("Goal Money ? : "))
    per=eval(input("Percent ? : "))
    year=eval(input("Year ? : "))
    month=goal/(1+(per*0.01)/12)**(year*12)
    print(month)

def bmi():
    weight=eval(input("Weight ? : "))
    height=eval(input("Height ? : "))
    foweight=weight*0.45359237
    inheight=height*0.0254
    print("BMI : ",round(foweight/inheight**2,4))

def temp():
    temper=eval(input("Input -58F ~ 41F temperature : "))
    mph=eval(input("Input mph : "))
    chill = 35.74+(0.6215*temper)-(35.75*(mph**0.16))+(0.4275*temper*(mph**0.16))
    print("Wind chill : ",round(chill,5))
