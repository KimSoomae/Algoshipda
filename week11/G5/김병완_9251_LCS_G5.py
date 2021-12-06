import sys; sys.stdin = open('9251_LCS_G5.txt', 'r')
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

tmp = []
for r in range(len(A) + 1):
    tmp.append(max(dp[r]))
print(max(tmp))
