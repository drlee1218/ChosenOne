def solution(my_str, n):
    answer = []
    i=0
    while(i<len(my_str)):
        answer.append(my_str[i:i+n])
        i+=n
        
    #문자열 슬라이싱 str이라는 문자열이 있으면 start인덱스부터 end인덱스까지 추출하고 싶으면 str[start:end+1:step] step은 문자열을 건너뛰면서 추출할때 사용 기본은 1 
    #my_str[i:i + n]에서 마지막 슬라이싱이 n보다 적은 길이일 경우, 빈 문자열이 아닌 그 남은 부분을 정확히 반환
    
    return answer