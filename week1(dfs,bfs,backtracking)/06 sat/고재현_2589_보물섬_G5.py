# python3으로 하면 시간초과 / pypy로 하면 통과
from collections import deque


def bfs(si,sj):
    visited = [[0] * m for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    max_val = 0
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 'L' and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    max_val = visited[ni][nj]
                    q.append((ni,nj))
    return max_val -1


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

ans = 0
for si in range(n):
    for sj in range(m):
        if arr[si][sj] == 'L':
            ans = max(ans, bfs(si,sj))

print(ans)


