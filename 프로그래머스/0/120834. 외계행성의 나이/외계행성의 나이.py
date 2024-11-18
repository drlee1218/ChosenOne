def solution(age):
    n = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j'
    }
    a=list(str(age))
           
    for j in range(len(a)):
        a[j]=n[int(a[j])]
                
    
    return ''.join(a)