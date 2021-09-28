import sys
sys.stdin = open('김병완_2591_숫자카드_G5.txt', 'r')

input = sys.stdin.readline

nums = list(input().rstrip())
grand = ''
parent = ''
num = ''
dp = [0] * len(nums)
# dp 초기값 설정
dp[0] = 1

# if nums[1] == 0:
#    dp[1] = 1
if (nums[1] != '0' and 1 <= int(nums[0]) < 3) or (nums[0] == '3' and 1 <= int(nums[1]) <= 4):
    dp[1] = 2
else:
    dp[1] = 1

# for i in range(2, len(nums)):
#     grand = nums[i - 2]
#     parent = nums[i - 1]
#     num = nums[i]
#
#     if int(num) == 0 and int(parent) == 0 or int(num) == 0 and int(parent) > 3:
#         break
#     elif int(num) == 0 and 0 < int(parent) <= 3:
#         dp[i] = dp[i - 2]
#     elif int(parent) == 0:
#         dp[i] = dp[i - 1]
#     elif int(grand + parent) <= 34 and int(parent + num) <= 34:
#         dp[i] = dp[i - 2] + dp[i - 1]
#     elif int(grand + parent) <= 34 and int(parent + num) > 34:
#         dp[i] = dp[i - 1]
#     elif int(grand + parent) > 34 and int(parent + num) <= 34:
#         dp[i] = dp[i - 2] + dp[i - 1]
#     elif int(grand + parent) > 34 and int(parent + num) > 34:
#         dp[i] = dp[i - 1]

for i in range(2, len(nums)):
    parent = nums[i - 1]
    num = nums[i]

    if int(num) == 0 and int(parent) == 0 or int(num) == 0 and int(parent) > 3:
        break
    elif int(num) == 0 and 0 < int(parent) <= 3:
        dp[i] = dp[i - 2]
    elif int(parent) == 0:
        dp[i] = dp[i - 1]
    elif int(parent + num) <= 34:
        dp[i] = dp[i - 2] + dp[i - 1]
    elif int(parent + num) > 34:
        dp[i] = dp[i - 1]

print(dp[len(nums) - 1])