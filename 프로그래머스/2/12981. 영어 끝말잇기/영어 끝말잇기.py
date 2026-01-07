def solution(n, words):
    answer = [0, 0]
    l=len(words)
    for i in range(0, l):
        for j in range(0, i):
            if words[i]==words[j]:
                answer=[i%n+1, i//n+1]
                return answer
        if i>0:    
            if words[i-1][-1] != words[i][0]:
                answer=[i%n+1, i//n+1]
                return answer
                
    return answer