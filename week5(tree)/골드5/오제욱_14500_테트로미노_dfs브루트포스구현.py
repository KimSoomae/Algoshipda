import sys; read = sys.stdin.readline
from pprint import pprint
N, M = map(int,read().split())
Map = [list(map(int,read().split())) for _ in range(N)]

def rotate(pi):
    #90도 회전
    ret = [[0]*len(pi) for _ in range(len(pi[0]))]
    for x, _ in enumerate(pi):
        for y, __ in enumerate(_):
            ret[y][len(pi)-x-1] = __
    return ret

nomis = []
nomis_pure = [[[1,1,1,1]],[[1,1],[1,1]],[[1,1,1],[1,0,0]],[[0,1,1],[1,1,0]],[[1,1,0],[0,1,1]],[[1,1,1],[0,1,0]],[[1,1,1],[0,0,1]]]
for nomi in nomis_pure:
    ret = [nomi]
    k = rotate(nomi)
    while k not in ret:
        ret.append(k)
        k = rotate(k)

    nomis.extend(ret)

anw = 0
for nomi in nomis:
    for x in range(N-len(nomi)+1):
        for y in range(M-len(nomi[0])+1):
            cnt = 0
            for nx, _ in enumerate(nomi):
                for ny, __ in enumerate(_):
                    cnt += __*Map[nx+x][ny+y]

            if cnt > anw:
                anw = cnt

print(anw)


''':var
가능한 테트로미노가 4 블럭으로 만들 수 있는 모든 경우라 
dfs로도 풀 수 있다.
그리고 더 빠름
'''

# from sys import stdin
#
# getline = stdin.readline
#
# maxVal = 0
# N, M = map(int, getline().split())
# matrix = [list(map(int, getline().split())) for row in range(N)]
#
# visited = [[False] * M for row in range(N)]
# rDir = [-1, 0, 1, 0]
# cDir = [0, -1, 0, 1]
#
#
# def movePossible(r: int, c: int):
#     return (0 <= r and r < N and 0 <= c and c < M) and (visited[r][c] == False)
#
#
# def dfs(r: int, c: int, curVal: int, steps: int):
#     global maxVal
#     if(curVal + maxValInMatrix * (4 - steps) <= maxVal):
#         return
#
#     if(steps == 4):
#         maxVal = max(maxVal, curVal)
#         return
#
#     for i in range(4):
#         nr = r + rDir[i]
#         nc = c + cDir[i]
#         if(movePossible(nr, nc)):
#             if(steps == 2):
#                 visited[nr][nc] = True
#                 dfs(r, c, curVal + matrix[nr][nc], steps + 1)
#                 visited[nr][nc] = False
#
#             visited[nr][nc] = True
#             dfs(nr, nc, curVal + matrix[nr][nc], steps + 1)
#             visited[nr][nc] = False
#
#
# maxValInMatrix = max(map(max, matrix))
#
# for row in range(N):
#     for col in range(M):
#         visited[row][col] = True
#         dfs(row, col, matrix[row][col], 1)
#         visited[row][col] = False
#
# print(maxVal)