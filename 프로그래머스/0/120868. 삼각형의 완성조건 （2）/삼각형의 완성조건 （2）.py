def solution(sides):
    answer = 0
    maxs=max(sides)
    mins=min(sides)
    answer=2*mins-1#maxs+mins-maxs+mins-1
        
    return answer