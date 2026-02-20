def solution(schedules, timelogs, startday):
    def to_min(t):
        return (t // 100) * 60 + (t % 100)

    n = len(schedules)
    answer = 0

    for i in range(n):
        limit = to_min(schedules[i]) + 10
        ok = True

        for j in range(7):
            day = (startday + j) % 7

            # 토(6), 일(0)은 제외
            if day == 6 or day == 0:
                continue

            if to_min(timelogs[i][j]) > limit:
                ok = False
                break

        if ok:
            answer += 1

    return answer