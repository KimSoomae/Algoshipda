import sys
sys.stdin = open('input.txt')

# f(4) = f(3) + f(2) + f(1) -> 7
# f(3) = f(2) + f(1) + f(0) -> 4 
# f0 = 1 f1 = 1 f2 = 2
# 3 4 5  6 7 
# 4 7 13 24 44

TC = int(input())
for case_number in range(1, TC+1):
    n = int(input())
    memo = [1, 1, 2]
    for i in range(3, n+1):
        memo.append(memo[i-1] + memo[i-2] + memo[i-3])
    print(memo[n])