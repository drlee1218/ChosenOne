def solution(points, routes):
    from collections import defaultdict

    # 포인트 번호 → 좌표
    point = {i+1: tuple(points[i]) for i in range(len(points))}

    # 한 로봇의 전체 이동 경로 생성
    def build_path(route):
        path = []
        r, c = point[route[0]]
        path.append((r, c))

        for i in range(1, len(route)):
            tr, tc = point[route[i]]

            # r 먼저 이동
            while r != tr:
                r += 1 if tr > r else -1
                path.append((r, c))

            # c 이동
            while c != tc:
                c += 1 if tc > c else -1
                path.append((r, c))

        return path

    # 모든 로봇 경로 생성
    robot_paths = [build_path(route) for route in routes]

    max_time = max(len(p) for p in robot_paths)
    danger = 0

    # 시간별 충돌 체크
    for t in range(max_time):
        counter = defaultdict(int)

        for path in robot_paths:
            if t < len(path):          # 아직 센터 안에 있는 로봇만
                counter[path[t]] += 1

        # 같은 좌표에 2대 이상이면 위험
        for cnt in counter.values():
            if cnt >= 2:
                danger += 1

    return danger
