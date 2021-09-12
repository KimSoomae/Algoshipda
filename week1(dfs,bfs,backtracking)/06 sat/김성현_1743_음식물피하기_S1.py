import sys
sys.stdin = open('input.txt')

C, R, K = map(int, input().split())

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def dfs(c, r):
    global area
    area += 1
    visited[c][r] = 1
    for i in range(4):
        new_c = c + dc[i]
        new_r = r + dr[i]
        if 1 <= new_c <= C and 1 <= new_r <= R:
            if board[new_c][new_r] == 1 and visited[new_c][new_r] == 0:
                dfs(new_c, new_r)
                


board = [[0]*(R+1) for _ in range(C+1)]
for i in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

visited = [[0]*(R+1) for _ in range(C+1)]
print(board)

max_area = 0

for i in range(1, C+1):
    for j in range(1, R+1):
        sc = i
        sr = j
        if board[i][j] == 1 and visited[i][j] == 0:
            area = 0
            dfs(i, j)
            if area > max_area:
                max_area = area


print(max_area)