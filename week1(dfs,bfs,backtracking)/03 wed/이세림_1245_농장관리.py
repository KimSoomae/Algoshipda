import sys
sys.stdin = open('1245.txt', 'r')

def dfs(x, y):
    farm[x][y] = 0
    for k in range(4):
        X = x + r[k]
        Y = y + c[k]
        if (0 <= X < N) and (0 <= Y < M) and farm[X][Y] != 0:
            dfs(X, Y)

N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
r = [0, 0, -1, 1]
c = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if farm[i][j] != 0:
            dfs(i, j)
            cnt += 1

print(cnt)
