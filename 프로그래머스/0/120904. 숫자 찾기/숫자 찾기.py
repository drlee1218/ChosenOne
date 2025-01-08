def solution(num, k):
    answer = -1
    for i in str(num):
        if i == str(k):
            answer=list(str(num)).index(i)+1
    
    return answer