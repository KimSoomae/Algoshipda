import sys; sys.stdin = open('2638_치즈_G4.txt', 'r')

from collections import deque
input = sys.stdin.readline

def init(r, c, arr):
    section = [[] for _ in range(N)]
    for row in range(N):
        section[row] = arr[row][:]
    Q = deque()
    Q.append((r, c))
    while Q:
        row, col = Q.popleft()
        if section[row][col]: continue
        section[row][col] = 2

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if arr[nr][nc] == 1: section[nr][nc] = 1
            if section[nr][nc]: continue
            Q.append((nr, nc))
    return section

def div_section():
    Q = deque()
    for i in range(N):
        for j in range(M):
            if sect[i][j] == 0:
                for k in range(4):
                    ni = i + dr[k]
                    nj = j + dc[k]
                    if sect[ni][nj] == 2:
                        Q.append((i, j))
                        break
                while Q:
                    row, col = Q.popleft()
                    sect[row][col] = 2
                    # 변수는 간섭 받지 않는 걸로 신중히 만들자
                    for direction in range(4):
                        nr = row + dr[direction]
                        nc = col + dc[direction]
                        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
                        if sect[nr][nc]: continue
                        Q.append((nr, nc))


def melting(arr):
    tmp = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt = 0
                for k in range(4):
                    ni = i + dr[k]
                    nj = j + dc[k]
                    if sect[ni][nj] == 2:
                        cnt += 1
                    if cnt == 2:
                        break
                if cnt == 2:
                    tmp.append((i, j))
    for x, y in tmp:
        sect[x][y] = 2


def isleft():
    for i in range(N):
        for j in range(M):
            if sect[i][j] == 1:
                return True
    return False

N, M = map(int, input().split())
cheezeInTheAir = [list(map(int, input().split())) for _ in range(N)]
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
time = 0
r, c = -1, -1
for i in range(N):
    for j in range(M):
        if cheezeInTheAir[i][j] == 0:
            r, c = i, j
            break
    if (r, c) != (-1, -1):
        break

sect = init(r, c, cheezeInTheAir)
while isleft():
    melting(cheezeInTheAir)
    time += 1
    div_section()

print(time)
