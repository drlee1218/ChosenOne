def solution(n, w, num):
    # num 위치
    row = (num - 1) // w
    idx = (num - 1) % w

    if row % 2 == 0:      # 짝수층: 왼 → 오
        col = idx
    else:                 # 홀수층: 오 → 왼
        col = w - 1 - idx

    total_rows = (n - 1) // w
    count = 1  # 자기 자신 포함

    # 위층 확인
    for r in range(row + 1, total_rows + 1):
        if r % 2 == 0:    # 짝수층
            idx_above = col
        else:             # 홀수층
            idx_above = w - 1 - col

        box_num = r * w + idx_above + 1
        if box_num <= n:
            count += 1

    return count