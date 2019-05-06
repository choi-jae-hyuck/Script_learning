num=eval(input())
result=[]
for i in range(num):
    osel=eval(input())
    a=input()
    b=input()
    wb=0
    bw=0
    for j in range(osel):
        if a[j] is 'W' and b[j] is 'B':
            wb +=1
        elif a[j] is 'B' and b[j] is 'W':
            bw+=1
    if wb<bw:
        result.append(bw)
    else:
        result.append(wb)
for i in range(num):
    print(result[i])