import sys
sys.stdin = open('김병완_9095_123더하기_S3.txt', 'r')
input = sys.stdin.readline

for tc in range(int(input())):
    num = int(input())
    dp = [0, 1, 2, 4] + [0] * (num - 3)
    for i in range(4, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[num])
