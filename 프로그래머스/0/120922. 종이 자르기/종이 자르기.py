def solution(M, N):
    if M-1==0:
        answer=N-1
    else:
        answer = (M-1)+M*(N-1)
    return answer