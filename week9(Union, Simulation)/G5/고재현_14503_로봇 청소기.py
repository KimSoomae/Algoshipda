def robot(i, j, d):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    global ans
    if arr[i][j] == 0:
        arr[i][j] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        ni = i + di[nd]
        nj = j + dj[nd]
        if arr[ni][nj] == 0:
            robot(ni, nj, nd)
            return
        d = nd
    nd = (d + 2) % 4
    ni = i + di[nd]
    nj = j + dj[nd]
    if arr[ni][nj] == 1:
        return
    robot(ni, nj, d)


n, m = map(int, input().split())
i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
robot(i, j, d)
print(ans)