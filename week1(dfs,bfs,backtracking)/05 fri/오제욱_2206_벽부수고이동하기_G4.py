import sys; readline = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    Q = deque([[0,0,True]])
    while Q:
        x,y, flag = Q.popleft()
        for _ in range(4):
            nx,ny = x+dx[_], y+dy[_]
            if N>nx>=0 and M>ny>=0:
                if not Map[nx][ny]:
                    if flag and not visited[nx][ny][0]:
                        visited[nx][ny][0] = visited[x][y][0] + 1
                        Q.append([nx,ny,flag])
                    elif not flag and not visited[nx][ny][1]:
                        visited[nx][ny][1] = visited[x][y][1] + 1
                        Q.append([nx,ny,flag])
                elif Map[nx][ny] and flag and not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    Q.append([nx,ny,False])
            if any(visited[-1][-1]):
                return visited[-1][-1]

    return visited[-1][-1]

N, M = map(int,readline().split())
Map = [list(map(int,readline().rstrip())) for _ in range(N)]
numvisit = bfs()
if any(numvisit):
    print(min(list(filter(lambda x: x if x>0 else None, numvisit))))
else:
    print(-1)