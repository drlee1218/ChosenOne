import math
def solution(n):
    answer=0
    for i in range(1, 11):
        if n>=math.factorial(i) and math.factorial(i+1)>n:
            answer = i
            break
    return answer