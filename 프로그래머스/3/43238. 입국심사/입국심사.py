def solution(n, times):
    left = 1
    right = max(times) * n  #최악의 경우
    
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        #mid 시간 동안 처리 가능한 인원
        people = sum(mid // time for time in times)
        
        if people >= n:
            answer = mid
            right = mid - 1  
        else:
            left = mid + 1   #시간 부족
    
    return answer