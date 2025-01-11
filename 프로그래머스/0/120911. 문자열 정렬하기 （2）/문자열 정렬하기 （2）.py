def solution(my_string):
    swap=my_string.lower()
    swaplist=list(swap)
    swaplist.sort() 
    return ''.join(swaplist)
#sort는 리스트 자체를 정렬하고 sorted는 문자열, 리스트, 튜플 등 다양한 데이터 타입을 정렬한 뒤 이를 새로운 리스트로 반환한다.