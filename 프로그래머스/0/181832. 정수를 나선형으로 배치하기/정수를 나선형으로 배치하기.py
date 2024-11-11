def solution(n):
    answer= [[0] * n for _ in range(n)]
    directions=[(0,1), (1,0), (0, -1), (-1, 0)]
    x, y= 0, 0
    c_d= 0
    
    for i in range(1, n*n+1):
        answer[x][y]= i
        dx, dy= directions[c_d]
        nx, ny= x+dx, y+dy
        
        if nx<0 or nx>n-1 or ny<0 or ny>n-1 or answer[nx][ny]!=0:
            c_d= (c_d+1)%4
            dx, dy= directions[c_d]
            nx, ny = x+dx, y+dy
            
        x=nx
        y=ny
        
           
    return answer