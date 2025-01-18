def solution(numlist, n):
    answer=[]
    answer = sorted(numlist, key= lambda x: (abs(n-x), -x))#sotred의 key옵션을 이용한 다중 기준 정렬법 1기준을 중심으로 정렬하고 만약 같으면 뒤 기준을 중심으로 정렬하는것
    
    return answer