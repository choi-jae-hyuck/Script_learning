def hotel():
    while_num=input()
    while_num=int(while_num)
    SON = []
    for i in (0,while_num):
        list=input()
        list=list.split()
        H=int(list[0])
        W=int(list[1])
        N=int(list[2])
        for i in(0,W):
            for j in (0,H):
                N-=1
                if N == 0:
                    SON.append(j*100+i+1)
    for i in (0,while_num):
        print(SON[i])
