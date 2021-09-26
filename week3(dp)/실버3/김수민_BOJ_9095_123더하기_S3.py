T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if n <= 3:
        print(dp[n])
    else:
        for i in range(4, n + 1):
            # i-1의 경우 1을 추가해서 만드는 경우, i-2은 2를 추가해서 만드는 경우, i-3은 3을 추가해서 만드는 경우
            dp[i] = dp[i-1] + dp[i - 2] + dp[i - 3]
        print(dp[n])
