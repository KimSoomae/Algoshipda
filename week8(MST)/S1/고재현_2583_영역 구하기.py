from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visit[si][sj] = True
    cnt = 1
    while q:
        i, j = q.popleft()
        for z in range(4):
            ni, nj = i + di[z], j + dj[z]
            if 0 <= ni < m and 0 <= nj < n:
                if arr[ni][nj] == 0 and not visit[ni][nj]:
                    q.append((ni, nj))
                    visit[ni][nj] = True
                    cnt += 1

    return cnt


m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    start_i = m - y1 -1
    start_j = x1
    i_count = y2-y1
    j_count = x2 - x1
    for ii in range(i_count):
        for jj in range(j_count):
            arr[start_i-ii][start_j+jj] = 1


visit = [[False] * n for _ in range(m)]
ans = []
num = 0
for si in range(m):
    for sj in range(n):
        if arr[si][sj] == 0 and not visit[si][sj]:
            num += 1
            ans.append(bfs(si, sj))


print(num)
print(' '.join(map(str,sorted(ans))))
