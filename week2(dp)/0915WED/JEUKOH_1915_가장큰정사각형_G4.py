import sys; readline = sys.stdin.readline
n, m = map(int,readline().split())
Map = list(readline().rstrip() for _ in range(n))

dp = [[0]*(m+1) for _ in range(n+1)]

max_b = 0
for x in range(1,n+1):
    for y in range(1,m+1):
        if Map[x-1][y-1] == '1':
            dp[x][y] = min(dp[x][y-1],dp[x-1][y],dp[x-1][y-1])+1
            if max_b < dp[x][y]:
                max_b = dp[x][y]

print(max_b**2)
