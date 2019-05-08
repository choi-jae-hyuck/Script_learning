def prime():
    result=[]
    num=0
    number=2
    while True:
        correct = True
        if num is 100:
            break
        for i in range(2,number):
            if number%i is 0:
                correct=False
        if correct is True:
            a=0
            for i in str(number):
                a+=1
            co = True
            for i in range(a):
                if str(number)[i] is not str(number)[a-1-i]:
                    co=False
            if co is True:
                result.append(number)
                num+=1

        number+=1
    for i in range(10):
        print("{0: >7}{1: >7}{2: >7}{3: >7}{4: >7}{5: >7}{6: >7}{7: >7}{8: >7}{9: >7}".format(result[i*10+0],result[i*10+1],result[i*10+2],result[i*10+3],result[i*10+4],result[i*10+5],result[i*10+6],result[i*10+7],result[i*10+8],result[i*10+9]))
prime()