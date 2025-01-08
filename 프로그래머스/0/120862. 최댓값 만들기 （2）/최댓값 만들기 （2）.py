def solution(numbers):
    answer = []
    m=[]
    p=[]
    ne=0
    po=0
    for i in numbers:
        if i<=0:
            m.append(i)
        else:
            p.append(i)
                 
    m.sort()
    p.sort()
    
    if len(p)==1 and len(m)==1:
        return m[0]*p[0]
    
    if len(p)>=2:
        po=p[-1] * p[-2] 
        
    if len(m)>=2:
        ne=m[0] * m[1] 
    
    

    if ne>po:
            return ne
    return po