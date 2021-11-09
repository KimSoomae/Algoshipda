from collections import deque
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(si,sj):
    move_q = deque()
    q.append([si, sj])
    c[si][sj] = 1
    people, cnt = 0, 0
    while q:
        i, j = q.popleft()
        move_q.append([i, j])
        people += arr[i][j]
        cnt += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not c[ni][nj]:
                if l <= abs(arr[i][j] - arr[ni][nj]) <= r:
                    c[ni][nj] = cnt
                    q.append([ni, nj])

    while move_q:
        i, j = move_q.popleft()
        arr[i][j] = people // cnt

    if cnt == 1:
        return 0
    return 1

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    q = deque()
    c = [[0]*n for _ in range(n)]
    cnt = 0
    for si in range(n):
        for sj in range(n):
            if not c[si][sj]:
                cnt += bfs(si, sj)
    if not cnt:
        break
    ans += 1

print(ans)