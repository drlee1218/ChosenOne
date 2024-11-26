from collections import deque
def solution(numbers, direction):
    n=deque(numbers)
    if direction=='right':
         n.rotate(1)  
    else:
         n.rotate(-1)   
                
    return list(n)