def solution(n):
    
    answer=0
    for j in range(1,n+1):
        numbers=0
        for i in range(1, j+1):
            if j%i==0:
                numbers+=1
        if numbers>=3:
            answer+=1
            
    return answer