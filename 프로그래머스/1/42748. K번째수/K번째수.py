def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sliced = array[i-1:j]      # 1. 자르기
        sliced.sort()              # 2. 정렬
        answer.append(sliced[k-1]) # 3. k번째
        
    return answer