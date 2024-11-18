def solution(angle):
    if angle==90:
        answer=2
    elif angle==180:
        answer=4
    else:
        answer = 3 if angle>90 else 1
    return answer