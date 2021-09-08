import sys
sys.stdin = open('input.txt')
from pprint import pprint
sys.setrecursionlimit(10**6)

N = int(input())
board = [[0]*(N+1)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    global cnt
    board[y][x] = 0
    cnt += 1

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y <= N and 0 <= new_x <= N:
            if board[new_y][new_x] == 1:
                dfs(new_y, new_x)



for i in range(N):
    column = [0] + list(map(int, input()))
    board.append(column)


result = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

print(len(result))
for num in sorted(result):
    print(num)