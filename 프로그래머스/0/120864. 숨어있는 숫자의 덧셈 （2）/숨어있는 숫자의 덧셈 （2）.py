def solution(my_string):
    answer = 0
    s=[]
    for i in my_string:
        if i.isdigit():
            s.append(i)
        else:
            if s:
                answer+=int(''.join(s))
                s=[]
    if s:        
        answer+=int(''.join(s))
        
    return answer