num=eval(input())
result=[]
for i in range(num):
    element=input()
    element=element.split()
    a,b=int(element[0]),int(element[2])
    answer=int(element[4])
    if element[1] is '+':
        ans= a + b
    elif element[1] is '-':
        ans= a - b
    elif element[1] is '*':
        ans= a * b
    elif element[1] is '/':
        ans=int( a / b )
    if ans - answer is 0:
        result.append("correct")
    else:
        result.append("wrong answer")
for i in range(num):
    print(result[i])