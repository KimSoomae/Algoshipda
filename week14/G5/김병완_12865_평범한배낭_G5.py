import sys; sys.stdin = open('12865_평범한배낭_G5.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
info = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = info[i]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(dp[N][K])