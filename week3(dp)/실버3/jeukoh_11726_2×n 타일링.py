from sys import stdin
read = stdin.readline
N = int(input())
mod = 10007
dp = [1]+[1]*N

for i in range(2,N+1):
    dp[i] = (dp[i-1]%mod+dp[i-2]%mod)%mod

print(dp[N])