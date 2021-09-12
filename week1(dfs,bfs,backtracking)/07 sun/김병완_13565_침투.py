import sys

# sys.stdin = open('김병완_13565_침투.txt', 'r')

sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split())
nodes = [list(input()) for _ in range(M)]

def dect(row, col):
    global result
    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]
    if row == M - 1:
        result = 'YES'
        return
    else:
        for dir in range(4):
            if 0 <= row + dr[dir] < M and 0 <= col + dc[dir] < N and nodes[row + dr[dir]][col + dc[dir]] == '0' and visited[row + dr[dir]][col + dc[dir]] == 0:
                visited[row + dr[dir]][col + dc[dir]] = 1
                dect(row + dr[dir], col + dc[dir])

result = 'NO'
cols = []
visited = [[0] * N for _ in range(M)]
for i in range(N):
    if nodes[0][i] == '0':
        cols.append(i)

for col in cols:
    dect(0, col)

print(result)
