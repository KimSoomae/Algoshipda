import sys; readline = sys.stdin.readline
N = int(input())
Map = [list(map(int,readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]


for x in range(N):
    for y in range(N):
        if x == 0 and y == 0:
            continue
        if x == 0:
            dp[x][y] = dp[x][y-1] if Map[x][y-1] > Map[x][y] else dp[x][y-1] + Map[x][y]-Map[x][y-1]+1
            continue
        if y == 0:
            dp[x][y] = dp[x-1][y] if Map[x-1][y] > Map[x][y] else dp[x-1][y] + Map[x][y] - Map[x-1][y] + 1
            continue
        tmp1 = dp[x][y-1] if Map[x][y-1] > Map[x][y] else dp[x][y-1] + Map[x][y]-Map[x][y-1]+1
        tmp2 = dp[x-1][y] if Map[x-1][y] > Map[x][y] else dp[x-1][y] + Map[x][y] - Map[x-1][y] + 1
        dp[x][y] = min(tmp1,tmp2)

print(dp[-1][-1])