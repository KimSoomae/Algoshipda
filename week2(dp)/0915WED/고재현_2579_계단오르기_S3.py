n = int(input())
stair = [0] * (n+1)
for k in range(1,n+1):
    stair[k] = int(input())

if n == 1: #n이 1일 때는 바로 출력
    print(stair[1])
elif n == 2: #n이 2일 때는 1과 2를 더해서 출력
    print(stair[1]+stair[2])
else:
    max_sum = [0] * (n+1)
    max_sum[1] = stair[1]
    max_sum[2] = stair[1] + stair[2] # 초기값 세팅

    for i in range(3, n+1):
        max_sum[i] = max(max_sum[i-3]+stair[i-1]+stair[i], max_sum[i-2]+stair[i])
    # 연속으로 3개를 갈 수 없고 최대 2칸까지 뛸 수 있으므로 경우의 수는 1. 내 1전 계단 + 3전 계단까지의 합 2. 내 2전까지의 합이므로 둘 중의 max값 고르기
    print(max_sum[n])

# 맨 처음 코드,, 왜 안되는건지 ,,
# def ans():
#     if n == 1:
#         return stairs[1]
#     elif n == 2:
#         return stairs[1] + stairs[2]
#     elif n == 3:
#         if stairs[1] < stairs[2]:
#             return stairs[2] + stairs[3]
#         else:
#             return stairs[1] + stairs[3]
#     else:
#         max_sum[1] = stairs[1]
#         order[1] = 1
#         max_sum[2] = stairs[1] + stairs[2]
#         order[2] = 1
#
#         if stairs[1] < stairs[2]:
#             max_sum[3] = stairs[2] + stairs[3]
#             order[3] = 2
#         else:
#             max_sum[3] = stairs[1] + stairs[3]
#             order[3] = 1
#
#         for i in range(4, n + 1):
#             if max_sum[i - 1] > max_sum[i - 2]:
#                 if order[i - 1] == i - 2:
#                     max_sum[i] = max_sum[i - 2] + stairs[i]
#                     order[i] = i - 2
#                 else:
#                     max_sum[i] = max_sum[i - 1] + stairs[i]
#                     order[i] = i - 1
#             else:
#                 max_sum[i] = max_sum[i - 2] + stairs[i]
#                 order[i] = i - 2
#         return max_sum[-1]
#
#
# n = int(input())
# stairs = [0] * (n+1)
# max_sum = [0] * (n+1)
# order = dict()
# for k in range(1,n+1):
#     stairs[k] = int(input())
#
# result = ans()
#
# print(order)
# print(result)





