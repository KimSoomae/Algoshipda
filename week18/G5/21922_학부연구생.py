input = open('input.txt').readline

from collections import deque
C, R = map(int, input().split()) 

dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(C)]

air = []
for c in range(C):
    for r in range(R):
        if board[c][r] == 9:
            air.append((c, r))

visited = [[0] * R for _ in range(C)]

def go(c, r, dir):
    pass

def bfs(arr):
    seat = 0
    for (c, r) in arr:
        if not visited[c][r]:
            visited[c][r] = 1
            seat += 1

        for i in range(4):
            nc = c + dc[i]; nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R:
                go(nc, nr, i)

                    




