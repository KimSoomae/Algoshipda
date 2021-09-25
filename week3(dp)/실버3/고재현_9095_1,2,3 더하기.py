t = int(input())
dp = [0] * 11
dp[1], dp[2], dp[3] = 1,2,4
for _ in range(t):
    n = int(input())
    for i in range(4,n+1):
        if dp[i] == 0:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])

# 풀이2: 시간, 메모리 똑같음
# t = int(input())
# dp = [0] * 11
# dp[1], dp[2], dp[3] = 1, 2, 4
# for i in range(4, 11):
#     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
# for _ in range(t):
#     n = int(input())
#     print(dp[n])
