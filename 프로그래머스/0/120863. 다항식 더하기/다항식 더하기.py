def solution(polynomial):
    answer = ''
    x=0
    s=0
    xlist=[]
    p=polynomial.replace(' ', '')
    for i in p.split('+'):
        if 'x' in i:
            xlist=i.split('x')
            if xlist[0]=='':
                x+=1
            else:
                x+=int(xlist[0])
        elif i.isdigit():
            s+=int(i)
    if s==0:
        if x==1:
            answer='x'
        else:
            answer=str(x)+'x'
    elif x==1:
            answer='x + '+str(s)
    elif x==0:
        answer=str(s)
    else:
        answer=str(x)+'x + '+str(s)

    return answer