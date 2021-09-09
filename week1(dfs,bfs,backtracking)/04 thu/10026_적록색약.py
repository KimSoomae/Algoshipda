import sys
sys.stdin = open("10026.txt", 'r')

def dfs(x, y):
    r = [0, 0, -1, 1]
    c = [1, -1, 0, 0]
    base[x][y] = 1
    for k in range(4):
        X = x + r[k]
        Y = y + c[k]
        if (0 <= X < N) and (0 <= Y < N) and base[X][Y] == 0 and data[X][Y] == data[x][y]:
            dfs(X, Y)

N = int(input())
data = [(' '.join(input())).split() for _ in range(N)]
base = [[0]*N for _ in range(N)]
cnt_1 = cnt_2 = 0

for i in range(N):
    for j in range(N):
        if base[i][j] == 0:
            dfs(i, j)
            cnt_1 += 1
print(cnt_1)

base = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j] == 'G':
            data[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if base[i][j] == 0:
            dfs(i, j)
            cnt_2 += 1
print(cnt_2)
