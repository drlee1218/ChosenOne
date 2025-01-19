def solution(chicken):
    answer = 0
    c=0
    for i in range(1, chicken+1):
        c+=1
        if c%10==0:
            c+=1
    answer=c//10
    return answer