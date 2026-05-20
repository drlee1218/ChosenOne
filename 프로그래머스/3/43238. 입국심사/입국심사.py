def solution(n, times):
    left = 1
    right = max(times) * n #최악의 경우의 수

    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 동안 처리 가능한 사람 수
        people = 0

        for t in times:
            people += mid // t

        # n명 이상 처리 가능
        if people >= n:
            answer = mid
            right = mid - 1

        # 아직 부족
        else:
            left = mid + 1

    return answer