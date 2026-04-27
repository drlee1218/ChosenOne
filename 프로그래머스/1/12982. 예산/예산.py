def solution(d, budget):
    d.sort()
    answer = 0
    for cost in d:
        if budget >= cost:
            budget -= cost
            answer += 1
        else:
            break
        
    return answer