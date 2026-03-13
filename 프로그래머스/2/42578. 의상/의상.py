from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    
    for _, kind in clothes:
        dic[kind] += 1
    
    answer = 1
    for i in dic.values():
        answer *= (i+1)
        
    return answer - 1