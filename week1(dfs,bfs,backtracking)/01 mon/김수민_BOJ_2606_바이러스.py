def bfs(N, V):
    cnt = 0
    visited[V] = 1
    q.append(V)
    while len(q) != 0:
        V = q.pop(0)
        for i in range(1, N + 1):
            if visited[i] == 0 and g[V][i] == 1:
                q.append(i)
                visited[i] = 1
        cnt += 1
    return cnt - 1



N = int(input())
M = int(input())
g = [[0] * (N + 1) for _ in range (N + 1)]
visited = [0] * (N + 1)
q = []
for i in range(M):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1
print(bfs(N, 1))