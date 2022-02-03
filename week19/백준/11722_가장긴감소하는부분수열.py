input = open('input.txt').readline

N = int(input())
board = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    s = []
    for j in range(i):
        if board[i] < board[j]:
            s.append(dp[j])
    if not s:
        continue
    else:
        dp[i] += max(s)
print(max(dp))