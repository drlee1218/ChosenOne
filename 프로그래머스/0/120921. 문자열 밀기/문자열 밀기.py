from collections import deque
def solution(A, B):

    la=deque(list(A))
    lb=list(B)
    c=0
    if A==B:
        return 0
    for i in range(1, len(A)):
        la.rotate(1)
        if list(la)==lb:
            return i
          
    return -1