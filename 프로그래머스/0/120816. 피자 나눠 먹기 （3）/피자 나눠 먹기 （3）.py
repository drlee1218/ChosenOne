

def solution(slice, n):
    answer = int(n/slice)
    if n%slice!=0:
        answer+=1
    return answer