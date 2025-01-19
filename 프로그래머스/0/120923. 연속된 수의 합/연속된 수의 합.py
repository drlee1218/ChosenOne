def solution(num, total):
    answer = []
    start=(total-num*(num-1)/2)/num
    
    return [start+i for i in range(num)]