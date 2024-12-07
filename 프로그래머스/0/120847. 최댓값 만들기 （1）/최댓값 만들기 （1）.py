def solution(numbers):
    a=max(numbers)
    numbers.remove(a)
    answer=a*max(numbers)
    return answer