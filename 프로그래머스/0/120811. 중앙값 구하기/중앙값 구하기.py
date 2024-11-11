def solution(array):
    array.sort()
    s=len(array)
    answer = array[int(s/2)]
    return answer