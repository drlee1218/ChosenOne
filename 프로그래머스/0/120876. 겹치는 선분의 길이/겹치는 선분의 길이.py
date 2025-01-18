def solution(lines):
    answer = 0
    point=[0]*201
    for s,e in lines:
        for i in range(s+100, e+100):
            point[i]+=1
            
    answer=sum(1 for i in point if i>1)
    
        
    return answer