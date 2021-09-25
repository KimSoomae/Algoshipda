import sys
sys.stdin = open('input.txt')

n = int(input())
lst = [0]* 100000
for i in range(n):
    lst[i] = int(input())

dp = [0] * 3

dp[0] = lst[0]
dp[1] = lst[1] + lst[0]
dp[2] = max(lst[2] + lst[0], dp[1], lst[1] + lst[2])

for i in range(3, n):
    dp.append(max(lst[i] + dp[i-2], lst[i] + lst[i-1] + dp[i-3], dp[i-1]))
print(dp[-1])



























"""
print(lst)
max_val = 0
for i in range(1 << n):
    case = ''
    for j in range(n):
        if i & (1<<j):
            case += '1'
        else:
            case += '0'
    if '111' in case:
        continue
    elif '000' in case: 
        continue
    else:
        val = 0
        case = list(case)
        for i in range(n):
            if case[i] == '1':
                val += lst[i]
        if val > max_val:
            max_val = val

print(max_val)
"""
