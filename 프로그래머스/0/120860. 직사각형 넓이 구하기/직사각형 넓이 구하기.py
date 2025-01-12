def solution(dots):
    x=[i[0] for i in dots]
    y=[j[1] for j in dots]
    
    g=max(x)-min(x)
    s=max(y)-min(y)
    
    return g*s