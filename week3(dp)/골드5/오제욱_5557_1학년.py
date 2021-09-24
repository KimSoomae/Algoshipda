import sys; readline = sys.stdin.readline
N = int(input())
numl = list(map(int,input().split()))

# 인풋 길이 N-1개를 의 0~20까지 표현하는 dp
# dp[x][y] -> x번째 수까지 +, -  연산을 하였을 때 y값이 나오는 경우의 수
dp = [[0]*21 for _ in range(N-1)]


dp[0][numl[0]] = 1
for idx,v in enumerate(numl[:-1]):
    if idx == 0:
        continue

    # 굳
    for j in range(21):
        if j-v >= 0 and dp[idx-1][j-v]: dp[idx][j] += dp[idx-1][j-v]
        if j+v <= 20 and dp[idx-1][j+v]: dp[idx][j] += dp[idx-1][j+v]
print(dp[-1][numl[-1]])