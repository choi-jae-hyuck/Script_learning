num=eval(input())
result=[]
for i in range(num):
    a = []
    money = 0
    trying=eval(input())
    for j in range(trying):
        a.append(input())
        a[j]=a[j].split()
        a[j] = [eval(x) for x in a[j]]
    for j in range(trying):
        max=0
        for k in range(3):
            if a[j][k]>max:
                max=a[j][k]
        money +=max
    result.append(money)
for i in range(num):
    print(result[i])