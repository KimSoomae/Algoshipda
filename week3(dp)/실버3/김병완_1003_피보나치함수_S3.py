import sys
sys.stdin = open('김병완_1003_피보나치함수_S3.txt', 'r')
input = sys.stdin.readline

for tc in range(int(input())):
    num = int(input())
    dp = [(1, 0)] + [0] * num
    if num >= 1:
        dp[1] = (0, 1)
    for i in range(2, num + 1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

    print(dp[num][0], dp[num][1])