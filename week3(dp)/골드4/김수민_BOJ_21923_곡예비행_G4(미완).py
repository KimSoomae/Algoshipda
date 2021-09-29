# 아직 미완
dy = [-1, 0, 1]
dx = [0, 1, 0]
anw = -10000000
def dfs(y, x, flag, sum):
    global anw, N, M
    visited[y][x] = 1
    if y == N-1 and x == M - 1:
        if sum > anw:
            anw = sum
        dp[flag][y][x]=anw
        return
    if dp[flag][y][x] != -10000000:
        if not (y == N - 1 and x == 0):
           return dp[flag][y][x]
    if flag == 0:
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M and visited[y][x]:
                continue
            if i == 2:
                dfs(ny, nx, 1, sum + fly[y][x] + fly[ny][nx])
                dp[1][ny][nx] = max(dp[flag][y][x] + fly[ny][nx], dp[flag][ny][nx])

            else:
                dfs(ny, nx, 0, sum + fly[ny][nx])
                dp[0][ny][nx] = max(dp[flag][y][x] + fly[ny][nx], dp[flag][ny][nx])


    else: # 하강 비행
        for i in range(1, 3):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M and visited[y][x]:
                continue
            dfs(ny, nx, 1, sum + fly[ny][nx])
            dp[1][ny][nx] = max(dp[flag][y][x] + fly[ny][nx], dp[flag][ny][nx])

    visited[y][x] = 0

N, M = map(int, input().split())
fly = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = []
dp = [[[-10000000 for _ in range(M)] for _ in range(N)] for _ in range(2)]
dp[0][N-1][0] = fly[N-1][0]
dfs(N-1, 0, 0, fly[N-1][0])
print(anw)