input = open('input.txt').readline

n, k = map(int,input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(0, n+1):
    for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] % 1000000000)
'''
0 1 2 3 4 5 6 7 8 9
--------------------
1 1 1 1 1 1 1 1 1 1 
1 2 3 4 5 6 7 8 9 10
1 3 6 10
'''
