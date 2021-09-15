import sys
from pprint import pprint

sys.setrecursionlimit(10000)
read = sys.stdin.readline

X, Y = list(map(int, read().split()))
Map = [list(map(int, read().split())) for _ in range(X)]
dp = [[-1] * Y for _ in range(X)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 0, 0에서 출발
def dfs(x, y):  # dp[x][y]에 4방향으로 갈수 있는 경우의 수 리턴
    # 목적지에 도착하면 1을 리턴
    if x == X - 1 and y == Y - 1:
        return 1
    if not dp[x][y] == -1:
        return dp[x][y]

    # 초기화하고
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동 가능하면 dfs를 보냄
        if X > nx >= 0 and Y > ny >= 0 and Map[nx][ny] < Map[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]




dfs(0, 0)
print(dp[0][0])
