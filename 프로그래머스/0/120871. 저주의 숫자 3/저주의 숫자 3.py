def solution(n):
    p=0
    for i in range(1, n+1):
        p+=1
        while p%3==0 or '3' in str(p):
            p+=1

    return p