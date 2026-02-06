from collections import deque

def solution(terrain_map):
    height_len = len(terrain_map)
    width_len = len(terrain_map[0])

    explored_flag = [[False] * width_len for _ in range(height_len)]
    drill_yield = [0] * width_len

    move_set = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def flood_scan(start_h, start_w):
        search_queue = deque()
        search_queue.append((start_h, start_w))
        explored_flag[start_h][start_w] = True

        cluster_volume = 1
        crossed_columns = {start_w}

        while search_queue:
            cur_h, cur_w = search_queue.popleft()
            for dh, dw in move_set:
                next_h, next_w = cur_h + dh, cur_w + dw
                if 0 <= next_h < height_len and 0 <= next_w < width_len:
                    if terrain_map[next_h][next_w] == 1 and not explored_flag[next_h][next_w]:
                        explored_flag[next_h][next_w] = True
                        search_queue.append((next_h, next_w))
                        cluster_volume += 1
                        crossed_columns.add(next_w)

        return cluster_volume, crossed_columns

    for h_idx in range(height_len):
        for w_idx in range(width_len):
            if terrain_map[h_idx][w_idx] == 1 and not explored_flag[h_idx][w_idx]:
                volume, column_set = flood_scan(h_idx, w_idx)
                for col_id in column_set:
                    drill_yield[col_id] += volume

    return max(drill_yield)
