input = open('input.txt').readline

n = int(input())
board = list(map(int, input().split()))

dp = [board[0]]
for i in range(len(board)-1):
    dp.append(max(dp[i]+board[i+1], board[i+1]))
print(max(dp))