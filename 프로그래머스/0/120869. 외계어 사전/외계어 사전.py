def solution(spell, dic):
    for i in dic:
        if sorted(spell)==sorted(i):
            return 1
    return 2