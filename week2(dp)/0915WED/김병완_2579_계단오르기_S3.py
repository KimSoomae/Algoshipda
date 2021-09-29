# import sys
#
# sys.stdin = open('김병완_2579_계단오르기.txt', 'r')
#
N = int(input())
# stair = []
# for i in range(N):
#     stair.append(int(input()))
#
# dp = []
# dp.append(stair[0])
# dp.append(max(stair[0] + stair[1], stair[1]))
# dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
#
# for j in range(3, N):
#     dp.append(max(dp[j - 3] + stair[j] + stair[j - 1], dp[j - 2] + stair[j]))
#
# print(dp[-1])

stair = [0] * (N + 3)
dp = [0] * (N + 3)

for i in range(N):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])
for i in range(3, N):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[N - 1])



