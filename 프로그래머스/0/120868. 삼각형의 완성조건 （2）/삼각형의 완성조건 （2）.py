def solution(sides):
    answer = 0
    maxs=max(sides)
    mins=min(sides)
    answer=maxs+mins-maxs+mins-1
        
    return answer