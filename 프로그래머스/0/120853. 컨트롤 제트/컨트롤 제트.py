def solution(s):
    answer = 0
    stack=[]
    for i in s.split():
        if i=='Z':
            if stack:
                answer-=stack.pop()
        else:
            num=int(i)
            stack.append(num)
            answer+=num
    
    return answer