import sys; read = sys.stdin.read
N, *score = map(int,read().split())
dp = [[0]*2 for _ in range(N+2)]
score = [0,0] + score
for idx in range(2,N+2):
    dp[idx][0] = max(dp[idx-2][0],dp[idx-2][1])+score[idx]
    dp[idx][1] = dp[idx-1][0]+score[idx]
print(max(dp[-1]))