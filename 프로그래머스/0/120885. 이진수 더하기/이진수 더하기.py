def solution(bin1, bin2):
    answer = ''
    o=0
    l=[]
    bsum=0
    m=max(len(bin1), len(bin2))
    bin1=bin1.zfill(m)
    bin2=bin2.zfill(m)
    for i in range(m-1,-1,-1):
        bsum=o+int(bin1[i])+int(bin2[i])
        l.append(str(bsum%2))
        o=bsum//2
    if o:
        l.append('1')
        
    l.reverse()
    answer=''.join(l)
    return answer