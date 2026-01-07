def solution(n):
    if n<=1:
        return n
    
    p0=0
    p1=1
    
    for i in range(2, n+1):
        p0, p1 = p1, (p0+p1)%1234567
    
    return p1
        
    