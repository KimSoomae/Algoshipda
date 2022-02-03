input = open('input.txt').readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)

for i in range(1, k+1):
    a = []
    for j in  coins:
        if j <= i and dp[i-j] != -1:
            a.append(dp[i-j])
    if not a:
        dp[i] = -1

    else:
        dp[i] = min(a) + 1

print(dp[k])
