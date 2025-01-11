def solution(my_string):
    swap=my_string.lower()
    swaplist=list(swap)
    swaplist.sort()
    return ''.join(swaplist)