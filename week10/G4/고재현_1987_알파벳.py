#ord, strip등 함수 잘 활용하기!
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt):
    global ans
    if cnt == 26:
        ans = 26
        return
    else:
        ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            num = to_num(nx, ny)
            if c[num] == 0:
                c[num] = 1
                dfs(nx, ny, cnt+1)
                c[num] = 0

def to_num(x, y):
    return ord(a[x][y]) - ord('A')

m, n = map(int, input().split())
a = [list(map(str, input().strip())) for _ in range(m)]
c, ans = [0]*26, 0

c[to_num(0, 0)] = 1
dfs(0, 0, 1)
print(ans)