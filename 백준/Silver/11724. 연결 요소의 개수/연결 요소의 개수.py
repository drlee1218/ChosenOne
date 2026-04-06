import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)