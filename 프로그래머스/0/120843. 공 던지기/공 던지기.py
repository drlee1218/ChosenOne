def solution(numbers, k):
    answer=numbers[(k*2-1)%len(numbers)-1]
        
    return answer