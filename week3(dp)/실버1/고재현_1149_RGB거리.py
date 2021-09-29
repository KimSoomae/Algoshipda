n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
for i in range(1, n):  # 두번째 집부터 시작
    cost[i][0] = min(cost[i - 1][1], cost[i - 1][2]) + cost[i][0]  # i+1 번째 집을 빨간색으로 칠할때의 최소값
    cost[i][1] = min(cost[i - 1][0], cost[i - 1][2]) + cost[i][1]  # i+1 번째 집을 초로색으로 칠할때의 최소값
    cost[i][2] = min(cost[i - 1][0], cost[i - 1][1]) + cost[i][2]  # i+1 번째 집을 파란색으로 칠할때의 최소값
print(min(cost[n - 1]))  # n번째 집을 빨간색, 파란색, 초록색 칠한 것 중 가장 적은 cost를 출력한다.


# 내 틀린 답..
# n = int(input())
# dp = [-1] * 1001
# sum_val = 0
#
# for i in range(1, n+1):
#     cost = list(map(int,input().split()))
#     min_val = 1000
#     for k in range(3):
#         if k != dp[i-1] and cost[k] < min_val:
#             min_val = cost[k]
#             min_idx = k
#     sum_val += min_val
#     dp[i] = min_idx
#
# print(sum_val)
