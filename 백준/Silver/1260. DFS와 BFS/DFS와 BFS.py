from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

def dfs(start):
    visited = [0] * (N + 1)
    def go(v):
        visited[v] = 1
        print(v, end=' ')
        for nv in graph[v]:
            if not visited[nv]:
                go(nv)
    go(start)
    print()

def bfs(start):
    visited = [0] * (N + 1)
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for nv in graph[v]:
            if not visited[nv]:
                visited[nv] = 1
                q.append(nv)

dfs(V)
bfs(V)
