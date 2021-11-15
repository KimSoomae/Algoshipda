import sys; sys.stdin = open('17090_미로탈출하기_G2.txt', 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(r, c):
    if visit[r][c]: return
    visit[r][c] = 1
    for i in range(4):
        if maze[r][c] == letter[i]:
            nr = r + direction[i][0]
            nc = c + direction[i][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                dp[r][c] = 1
                continue
            # if visit[nr][nc]: continue
            if dp[nr][nc]: dp[r][c] = 1
            dfs(nr, nc)
            dp[r][c] = dp[nr][nc]

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
letter = ['U', 'L', 'D', 'R']
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for i in range(N):
    for j in range(M):
        dfs(i, j)
result = 0
for i in range(N):
    result += sum(dp[i])

print(result)



