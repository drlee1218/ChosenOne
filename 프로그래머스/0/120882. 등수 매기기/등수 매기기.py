"""def solution(score):
    answer = []
    avg=[sum(s)/2 for s in score]
    sort_avg=sorted(avg, reverse=True)
    
    rank_dic={}
    rank=1
    for i,s in enumerate(sort_avg):
        if i>0 and sort_avg[i]!=sort_avg[i-1]:
            rank=i+1
        rank_dic[s]=rank
        

    for a in avg:
        answer.append(rank_dic[a])
    
    return answer"""
def solution(score):
    answer=[]
    l=sorted([sum(s) for s in score], reverse=True)
    return [l.index(sum(i))+1 for i in score]
#파이썬의 index함수는 중복되는 값이 나오면 첫번째 값을 리턴한다.