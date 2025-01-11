from collections import Counter
def solution(before, after):
    answer = 0
    if Counter(before)==Counter(after):
        answer=1
    return answer