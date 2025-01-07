def solution(numbers):
    answer = ''
    s=''
    for i in numbers:
        s+=i
        if s == 'one':
            answer+='1'
            s=''
        elif s=='two':
            answer+='2'
            s=''
        elif s=='three':
            answer+='3'
            s=''
        elif s=='four':
            answer+='4'
            s=''
        elif s=='five':
            answer+='5'
            s=''
        elif s=='six':
            answer+='6' 
            s=''
        elif s=='seven':
            answer+='7'
            s=''
        elif s=='eight':
            answer+='8'
            s=''
        elif s=='nine':
            answer+='9'
            s=''
        elif s=='zero':
            answer+='0'
            s=''
        else:
            continue
            
    return int(answer)