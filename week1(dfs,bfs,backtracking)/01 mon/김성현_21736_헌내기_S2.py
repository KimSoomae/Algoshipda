# 훈수환영합니다

import sys
sys.stdin = open('input.txt')
#-----------------------------------------------------
sys.setrecursionlimit(10**6)

def dfs(y, x):
    global cnt
    visited[y][x] = 1
    if board[y][x] == 'P':
        cnt += 1
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 1 <= new_y <= C and 1 <= new_x <= R:
            if visited[new_y][new_x] == 0 and board[new_y][new_x] != 'X':
                dfs(new_y, new_x)

C, R = map(int, input().split())

board = [[0] * (R + 1)]

for y in range(1, C+1):
    column = [0] + list(input())
    board.append(column)

    if 'I' in column:
        sy = y
        sx = column.index('I')

# 우, 좌, 상, 하
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
visited = [[0]*(R+1) for _ in range(C+1)]
cnt = 0

dfs(sy, sx)
if cnt == 0:
    print('TT')
else:
    print(cnt)

