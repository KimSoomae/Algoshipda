import sys
sys.stdin = open('input.txt')

n = int(input())
num_list = list(map(int, input().split()))

memo = [[0 for _ in range(21)] for _ in range(n+1)]
# memo : i번째 덧/뺄셈의 결과에서 0~20까지 각 숫자가 나온 횟수를 산정
memo[1][num_list[0]] = 1 #case에선 8이므로 8에 해당하는 값 +1

for i in range(1, n):
    for j in range(21):
        if memo[i][j] > 0:
            if 0 <= j - num_list[i] <= 20:
                memo[i+1][j-num_list[i]] += memo[i][j]
            if 0 <= j + num_list[i] <= 20:
                memo[i+1][j+num_list[i]] += memo[i][j]

print(memo[n-1][num_list[-1]])

""" 시간초과 
dp = [[num_list[0]]]
for i in range(1, n-1):
    temp = []
    for j in range(len(dp[i-1])):
        plus_value = dp[i-1][j] + num_list[i]
        minus_value = dp[i-1][j] - num_list[i]
        if 0 <= plus_value <= 20:
            temp.append(plus_value)
        if 0 <= minus_value <= 20:
            temp.append(minus_value)
    dp.append(temp)
print(dp[-1])
print(dp[-1].count(num_list[-1]))
"""