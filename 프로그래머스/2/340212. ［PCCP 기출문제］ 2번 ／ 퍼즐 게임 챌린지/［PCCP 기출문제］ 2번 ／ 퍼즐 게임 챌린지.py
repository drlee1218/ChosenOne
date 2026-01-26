def solution(diffs, times, limit):
    n = len(diffs)

    def can_clear(level):
        total = 0
        for i in range(n):
            if diffs[i] <= level:
                total += times[i]
            else:
                fail = diffs[i] - level
                total += (times[i] + times[i-1]) * fail + times[i]
            if total > limit:
                return False
        return True

    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_clear(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
