def solution(array):
    answer = 0
    for i in ''.join(map(str,array)):
        if i=='7':
            answer+=1
    return answer
#map(함수, 반복할계체) ,구분자.join은 리스트의 문자열을 구분자를 기준으로 연결해주는 함수