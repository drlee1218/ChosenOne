def solution(numbers):
    s=len(numbers)
    answer = [0]*s
    for i in range(s):
        answer[i]=numbers[i]*2
    return answer