N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(N + 1)]

dp[1][arr[0]] = 1

for j in range(1, N):
    for i in range(21):
        if dp[j][i] > 0:
            if 0 <= i - arr[j] <= 20:
                dp[j + 1][i - arr[j]] += (dp[j][i])

            if 0 <= i + arr[j] <= 20:
                dp[j + 1][i + arr[j]] += (dp[j][i])

print(dp[N - 1][arr[N - 1]])