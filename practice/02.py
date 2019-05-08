def Yatzee():
    while True:
        number=input()
        number=number.split()
        number=[int(x) for x in number]
        num=0
        four=0
        correct=True
        for i in range(4):
            if number[i]<number[i+1] and (number[i] is number[i+1] or number[i]+1 is number[i+1]):
                if(four>=0):
                    four+=1
                num=1
            elif number[i]>number[i+1]:
                if(four<=0):
                    four-=1
                num=-1
            elif number[i] is number[i+1]and (number[i] is number[i+1] or number[i]-1 is number[i+1]):
                if(four>0):
                    four+=1
                else:
                    four-=1
                num=0
        if four>=4 or four<=-4:
            print("YES")
        else:
            print("NO")
Yatzee()