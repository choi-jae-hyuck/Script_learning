def chess():
    board=[]
    for i in range(8):
        board.append(input())
        board[i]=list(board[i])
    num=0
    for i in range(8):
        for j in range(8):
            if board[i][j] is 'F' and (i+j)%2 is 0:
                num+=1
    return num
