def solution(my_string):
    answer = ''
    for i in my_string:
        if i in answer:
            i=''
        answer+=i
        
    return answer