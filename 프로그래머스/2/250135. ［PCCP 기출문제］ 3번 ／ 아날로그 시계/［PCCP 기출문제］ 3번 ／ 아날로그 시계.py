def solution(h1, m1, s1, h2, m2, s2):
    # 시각 → 초 변환
    def encode_time(h, m, s):
        return h * 3600 + m * 60 + s

    begin_tick = encode_time(h1, m1, s1)
    end_tick = encode_time(h2, m2, s2)

    alert_moments = set()

    # 초침-분침
    sm_gap = 360 / 5.9
    idx = 0
    while True:
        moment = idx * sm_gap
        if moment >= end_tick:
            break
        if begin_tick <= moment < end_tick:
            alert_moments.add(round(moment, 6))
        idx += 1

    # 초침-시침
    sh_gap = 360 / (719 / 120)
    idx = 0
    while True:
        moment = idx * sh_gap
        if moment >= end_tick:
            break
        if begin_tick <= moment < end_tick:
            alert_moments.add(round(moment, 6))
        idx += 1

    return len(alert_moments)
