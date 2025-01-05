def solution(array, n):
    answer = array[0]

    m=abs(n-array[0])
    
    for i in array:  
        if abs(n-i)<m:
            m=abs(n-i)
            answer=i
        elif abs(n-i)==m and i < answer:
            answer=i
            
    return answer