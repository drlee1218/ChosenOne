def solution(brown, yellow):
    answer = []
    s=yellow+brown
    for i in range(1, s//2+1):
        if s%i==0:
            j=s//i
            if i>=j:
                if (i-2)*(j-2)==yellow:
                    return [i,j]
    
    