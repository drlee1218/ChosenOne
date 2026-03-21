from collections import deque

def solution(n, wires):
    
    def bfs(start, graph, visited):
        q = deque([start])
        visited[start] = True
        count = 1
        
        while q:
            now = q.popleft()
            for next_node in graph[now]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
                    count += 1
        return count
    
    answer = n
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        
        # i번째 간선 제거하고 그래프 구성
        for j in range(len(wires)):
            if i == j:
                continue
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = [False] * (n+1)
        
        # 아무 노드에서 시작해서 한 쪽 크기 구하기
        size = bfs(1, graph, visited)
        
        diff = abs(size - (n - size))
        answer = min(answer, diff)
    
    return answer