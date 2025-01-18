def solution(lines):
    answer = 0
    point=[0]*201
    for s,e in lines:
        for i in range(s+100, e+100):
            point[i]+=1
            
    answer=sum(1 for i in point if i>1)
    
        
    return answer
"""집합을 이용한 풀이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    """