N = int(input())
board = [list(input()) for i in range(N)]

def check():
    max_c = 1
    
    #행 검사
    for i in range(N):
        c = 1 
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                c += 1
            else:
                c = 1
            max_c = max(max_c, c)
     
    #열 검사
    for j in range(N):
        c = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                c += 1
            else:
                c = 1
            max_c = max(max_c, c)
    return max_c

answer = 0
for i in range(N):
    for j in range(N):
        
        #오른쪽 교환
        if j+1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
         # 아래 교환
        if i+1 < N and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)
