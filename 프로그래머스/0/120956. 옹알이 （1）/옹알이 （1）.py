def solution(babbling):
    answer = 0
    b=['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for w in b:
            if w*2 not in i:
                i=i.replace(w,' ')
        i=i.replace(' ','')
        if i=='':
            answer+=1
    return answer