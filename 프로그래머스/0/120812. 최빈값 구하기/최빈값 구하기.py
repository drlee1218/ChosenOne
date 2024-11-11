from collections import Counter

def solution(array):
    c=Counter(array)
    max_count_elements = [item for item, freq in c.most_common() if freq == c.most_common(1)[0][1]]
    if len(max_count_elements)>1:
        answer=-1
    else:    
        answer = c.most_common(1)[0][0]
    
    return answer