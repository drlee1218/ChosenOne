import math
def solution(a, b):

    g=math.gcd(a,b)
    b=b/g
    while b%2==0:
        b=b//2
    while b%5==0:
        b=b//5
        
    return 1 if b==1 else 2
