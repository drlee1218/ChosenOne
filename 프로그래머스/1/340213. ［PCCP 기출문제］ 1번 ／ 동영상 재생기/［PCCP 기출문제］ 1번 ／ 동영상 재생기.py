def solution(video_len, pos, op_start, op_end, commands):
    # mm:ss -> 초
    def to_sec(t):
        m, s = map(int, t.split(":"))
        return m * 60 + s

    # 초 -> mm:ss
    def to_time(sec):
        return f"{sec // 60:02d}:{sec % 60:02d}"

    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    # 오프닝 구간 체크 함수
    def skip_opening(pos):
        if op_start <= pos <= op_end:
            return op_end
        return pos

    # 시작 시 오프닝 체크
    pos = skip_opening(pos)

    for cmd in commands:
        if cmd == "prev":
            pos = max(0, pos - 10)
        else: 
            pos = min(video_len, pos + 10)

        pos = skip_opening(pos)

    return to_time(pos)
