def solution(n):
    answer=0
    for i in range(n+1):
        answer+=(i if i%2==0 else 0)
    return answer