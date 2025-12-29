def solution(n):
    z=bin(n).count('1')
    n=n+1
    while bin(n).count('1')!=z:
        n=n+1
    
    return n