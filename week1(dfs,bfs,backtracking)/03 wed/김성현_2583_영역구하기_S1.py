import sys
sys.stdin = open('input.txt')
from pprint import pprint
M, N, Sqs = map(int, input().split())

board = [[0]* N for _ in range(M)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    global cnt
    board[y][x] = 1
    cnt += 1

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y <= M-1 and 0 <= new_x <= N-1:
            if board[new_y][new_x] == 0:
                dfs(new_y, new_x)



for i in range(Sqs):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            board[j][i] = 1

result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            cnt = 0
            dfs(i, j)
            result.append(cnt)
print(len(result))
for x in sorted(result):
    print(x, end=' ')



