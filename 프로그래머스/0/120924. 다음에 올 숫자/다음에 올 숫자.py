def solution(common):
    answer = 0
    if common[1]==(common[0]+common[2])/2:
        answer=common[len(common)-1]+common[1]-common[0]
    else:
        answer=common[len(common)-1]*(common[1]//common[0])
            
    return answer