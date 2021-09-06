import sys; readline = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(sx,sy):
    Map[sx][sy] = 2
    Q = deque([[sx,sy]])

    while Q:
        x,y = Q.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if M>nx>=0 and N>ny>=0 and not Map[nx][ny]:
                Map[nx][ny] = 2
                Q.append([nx,ny])



M, N = map(int,readline().split())

Map = [list(map(int,readline().rstrip())) for _ in range(M)]

for _ in range(N):
    if Map[0][_] == 0:
        bfs(0,_)

flag = False
for _ in range(N):
    if Map[-1][_] == 2:
        flag = True

print('YES' if flag else 'NO')
