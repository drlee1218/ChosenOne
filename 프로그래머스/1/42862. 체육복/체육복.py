def solution(n, lost, reserve):
    
    #여벌 있지만 도난도 당한 학생 처리
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for r in reserve_set:
        #앞 학샘에게 먼저 빌려줌
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        
        #앞 학생이 있으면 뒤 학생에게
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
        
    return n - len(lost_set)