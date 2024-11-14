def solution(n):
    answer=int(n/7)
    b=n%7
    if b!=0:
        answer=answer+1
    return answer