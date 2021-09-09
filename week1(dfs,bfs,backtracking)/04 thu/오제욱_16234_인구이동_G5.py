import sys; readline = sys.stdin.readline
from collections import deque
N,L,R = map(int,readline().split())
Map = [list(map(int,readline().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def getunion(x,y):
    visited[x][y] = False
    Q = deque([[x,y]])
    union = [[x,y]]
    while Q:
        x,y = Q.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if N > nx >= 0 and N > ny >= 0 and visited[nx][ny] and L <= abs(Map[nx][ny]-Map[x][y]) <= R:
                    visited[nx][ny] = False
                    union.append([nx,ny])
                    Q.append([nx,ny])

    return union

day = 0
while True:
    visited = [[True]*N for _ in range(N)]
    all_union = []
    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                tmp = getunion(x,y)
                if len(tmp) > 1:
                    all_union.append(tmp)

    for union in all_union:
        people = 0
        for coord in union:
            people += Map[coord[0]][coord[1]]
        people //= len(union)
        for coord in union:
            Map[coord[0]][coord[1]] = people

    if not all_union:
        break
    day += 1

print(day)