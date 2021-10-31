from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj, h):
    q = deque()
    q.append((si, sj))
    visit[si][sj] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] > h and not visit[ni][nj]:
                    q.append((ni, nj))
                    visit[ni][nj] = True


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [0]
min_val = 987654321
max_val = -1
for fi in range(n):
    for fj in range(n):
        if arr[fi][fj] > max_val:
            max_val = arr[fi][fj]
        if arr[fi][fj] < min_val:
            min_val = arr[fi][fj]


for h in range(min_val-1, max_val):
    visit = [[False] * n for _ in range(n)]
    safe_zone = 0
    for si in range(n):
        for sj in range(n):
            if arr[si][sj] > h and not visit[si][sj]:
                safe_zone += 1
                bfs(si, sj, h)

    ans.append(safe_zone)

print(max(ans))
