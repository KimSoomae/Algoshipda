import sys
sys.stdin = open('input.txt')


n = int(input())

memo = [0, 1, 2]
if n > 1:
    for i in range(3, n+1):
        memo.append(memo[i-1] + memo[i-2])
else:
    pass
print(memo)