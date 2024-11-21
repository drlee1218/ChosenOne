def solution(balls, share):
    s=1
    b=1
    for i in range(balls-share+1, balls+1):
        b*=i
    for i in range(1, share+1):
        s*=i
        
    return b//s