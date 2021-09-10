import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
board = [[0]*(R+1)]


for i in range(C):
    column = [0] + list(input())
    board.append(column)


dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]

White = 0
Blue = 0

visited = [[0] * (R+1) for _ in range(C+1)]

def dfs(c, r, x):
    global cnt
    cnt += 1
    visited[c][r] = 1
    for i in range(4):
        new_c = c + dc[i]
        new_r = r + dr[i]

        if 1 <= new_c <= C and 1 <= new_r <= R:
            if board[new_c][new_r] == x and not visited[new_c][new_r]:
                dfs(new_c, new_r, x)

for i in range(1, C+1):
    for j in range(1, R+1):
        if board[i][j] == 'W' and not visited[i][j]:
            cnt = 0
            dfs(i, j, 'W')
            White += cnt ** 2
            
cnt = 0            
for i in range(1, C+1):
    for j in range(1, R+1):
        if board[i][j] == 'B' and not visited[i][j]:
            cnt = 0
            dfs(i, j, 'B')
            Blue += cnt ** 2

print(White, Blue)