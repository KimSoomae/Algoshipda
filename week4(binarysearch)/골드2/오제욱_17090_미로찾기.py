import sys; readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int,readline().split())

Map = [list(readline().rstrip()) for _ in range(N)]
dp = [[False]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]


def dfs(x,y):

    if not 0 <= x < N or not 0 <= y < M:
        return True
    if visited[x][y]:
        return dp[x][y]
    visited[x][y] = True
    if Map[x][y] == 'D':
        dp[x][y] = dfs(x+1,y)
    elif Map[x][y] == 'U':
        dp[x][y] = dfs(x-1,y)
    elif Map[x][y] == 'L':
        dp[x][y] = dfs(x,y-1)
    else:
        dp[x][y] = dfs(x,y+1)

    return dp[x][y]


anw = 0
for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            dfs(x,y)
        anw += 1 if dp[x][y] else 0

print(anw)