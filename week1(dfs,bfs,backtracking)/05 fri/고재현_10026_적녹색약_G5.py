from collections import deque


def bfs(si, sj, word):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if color[ni][nj] == word and visited[ni][nj] is False:
                    visited[ni][nj] = True
                    q.append((ni, nj))


n = int(input())
color = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0
for si in range(n):
    for sj in range(n):
        if visited[si][sj] is False:
            cnt += 1
            bfs(si, sj, color[si][sj])
print(cnt, end=' ')

for change_i in range(n):
    for change_j in range(n):
        if color[change_i][change_j] == 'R':
            color[change_i][change_j] = 'G'

visited = [[False] * n for _ in range(n)]
cnt2 = 0
for si2 in range(n):
    for sj2 in range(n):
        if visited[si2][sj2] is False:
            cnt2 += 1
            bfs(si2, sj2, color[si2][sj2])
print(cnt2)
