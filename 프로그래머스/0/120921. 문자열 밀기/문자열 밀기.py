from collections import deque
def solution(A, B):

    la=deque(list(A))
    lb=list(B)
    c=0
    if A==B:
        return 0
    for i in range(len(A)):
        la.rotate(1)
        c+=1
        if list(la)==lb:
            return c
          
    return -1