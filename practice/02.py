num=eval(input())
result=[]
for i in range(num):
    a = []
    money = 0
    trying=eval(input())
    for j in range(trying):
        a.append(input())
        a=a[j*3].split()
    print(a)
    a=[eval(x) for x in a]
    for j in range(trying):
        max=0
        for k in range(3):
            if a[j*trying+k]>max:
                max=a[j*trying+k]
        money +=max
    result.append(money)
print(result)