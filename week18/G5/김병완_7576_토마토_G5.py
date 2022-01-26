import sys; sys.stdin = open('7576_토마토_G5.txt', 'r')
from collections import deque
input = sys.stdin.readline

def bfs():
    answer = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while Q:
        r, c, t = Q.popleft()
        # 여기서 board[r][c] = 1로 처리하면 중복으로 검색하는 게 많아짐
        answer = t - 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                Q.append((nr, nc, t + 1))
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                return -1
    return answer


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            Q.append((i, j, 1))

print(bfs())


