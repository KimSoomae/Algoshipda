# 시간 1076ms 왜 더 길고 복잡한데 더 짧은 시간이 걸리지? 서버차이?
import sys
input = sys.stdin.readline

num = int(input())
dp = [-1] * (num + 1)
dp[1] = 0

for i in range(1, num + 1):
    if dp[i] != -1:
        # if i + 1 == num or i * 2 == num or i * 3 == num: break
        if i + 1 <= num:
            if dp[i + 1] != -1:
                dp[i + 1] = min(dp[i] + 1, dp[i + 1])
            else:
                dp[i + 1] = dp[i] + 1
        if i * 2 <= num:
            if dp[i * 2] != -1:
                dp[i * 2] = min(dp[i] + 1, dp[i * 2])
            else:
                dp[i * 2] = dp[i] + 1
        if i * 3 <= num:
            if dp[i * 3] != -1:
                dp[i * 3] = min(dp[i] + 1, dp[i * 3])
            else:
                dp[i * 3] = dp[i] + 1

print(dp[num])

# 시간 1136ms
# import sys
# input = sys.stdin.readline
#
# num = int(input())
# dp = [1000001] * (num + 1)
# dp[1] = 0
#
# for i in range(1, num + 1):
#     if dp[i] != 1000001:
#         # if i + 1 == num or i * 2 == num or i * 3 == num: break
#         if i + 1 <= num:
#             dp[i + 1] = min(dp[i] + 1, dp[i + 1])
#         if i * 2 <= num:
#             dp[i * 2] = min(dp[i] + 1, dp[i * 2])
#         if i * 3 <= num:
#             dp[i * 3] = min(dp[i] + 1, dp[i * 3])
#
# print(dp[num])

## memoization이 미친 성능을 보여주는 것 같은데 구현하는 것 연습해보자.. later...