def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계 (안전하게 수정)
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if answer == '':
        answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계 (조건 수정)
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer