def solution(emergency):
    
    d={}
    s=sorted(emergency, reverse=True)
    
    for key, value in enumerate(s):
        d[value]=key+1
            
    for j in range(len(emergency)):
            emergency[j]=d[emergency[j]]
                
    return emergency