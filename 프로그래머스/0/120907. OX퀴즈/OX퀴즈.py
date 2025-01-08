def solution(quiz):
    answer = []
    for i in quiz:
        a,b=i.split('=')
        if eval(a)==int(b):
            answer.append('O')
        else:
            answer.append('X')
    return answer