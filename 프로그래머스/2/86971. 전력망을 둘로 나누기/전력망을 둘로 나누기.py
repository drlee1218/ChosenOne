from collections import deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    q = deque([start])
    count = 0
    while q:
        x = q.popleft()
        if visited[x]:
            continue
        else :
            visited[x] = True
            count += 1
        for i in graph[x]:
            q.append(i)
    return count



def solution(n, wires):
    answer = int(1e9)
    for i in range(n-1):
        graph = [[] for _ in range(n+1)]
        for j in range(n-1):
            if i == j :
                continue
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)

        a = bfs(wires[i][0] , graph, n)
        b = bfs(wires[i][1] , graph, n)
        answer = min(answer, abs(a - b))

    return answer