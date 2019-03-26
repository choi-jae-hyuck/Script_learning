def chess():
    board=[]
    for i in range(0,8):
        board.append(list(input()))
    num=0
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] is 'F' and (i+j)%2 is 0:
                num+=1
    return num
