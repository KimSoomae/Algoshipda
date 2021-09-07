from collections import deque


def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return cnt


node = int(input())
edge = int(input())
visited = [False] * (node + 1)
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1)-1)
