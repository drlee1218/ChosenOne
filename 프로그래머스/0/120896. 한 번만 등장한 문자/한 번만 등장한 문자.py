def solution(s):
    answer = list(s)
    r=[]
    ey=[]
    for i in answer:
        if i in r:
            r.remove(i)
            ey.append(i)
            
        
        else:
            if i not in ey:
                r.append(i)
        
            
    return ''.join(sorted(r))