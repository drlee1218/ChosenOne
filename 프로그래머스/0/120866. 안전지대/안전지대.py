def solution(board):
    answer = 0
    l=0
    a=len(board)
    b=len(board[0])
    for i in range(a):
        for j in range(b):
            if board[i][j]==1:
                l+=1
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        di=i+dx
                        dj=j+dy
                        if 0<=di<a and 0<=dj<b and board[di][dj]!=1:
                            board[di][dj]=2
            
    answer=sum(i.count(0) for i in board)
            
    
    return answer