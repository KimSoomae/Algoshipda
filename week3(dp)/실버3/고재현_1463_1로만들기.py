n = int(input())
# 질문 : dp = [0] * (n+1)로 하면 인덱스 에러가 나는데 왜 그런걸까?
dp = [0] * 1000001
dp[2], dp[3] = 1, 1

for i in range(4,n+1):
    if i % 6 == 0:
        dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])