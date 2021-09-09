from collections import deque


def bfs():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if tomato[ni][nj] == 0 and visited[ni][nj] is False:
                    visited[ni][nj] = True
                    tomato[ni][nj] = tomato[i][j] + 1
                    q.append((ni, nj))


def find(n, m, after):
    max1 = 0
    for find_i in range(n):
        for find_j in range(m):
            if after[find_i][find_j] == 0:
                return -1
            if after[find_i][find_j] > max1:
                max1 = after[find_i][find_j]
    return max1 - 1


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
for si in range(n):
    for sj in range(m):
        if tomato[si][sj] == 1:
            q.append((si, sj))
            visited[si][sj] = True

bfs()
print(find(n, m, tomato))
