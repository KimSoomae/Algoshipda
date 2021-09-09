import sys; readline = sys.stdin.readline
from collections import deque
N,L,R = map(int,readline().split())
Map = [list(map(int,readline().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def getunion(x,y):
    visited[x][y] = day
    Q = deque([[x,y]])
    union = [[x,y]]
    people = Map[x][y]
    while Q:
        x,y = Q.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if N > nx >= 0 and N > ny >= 0 and visited[nx][ny] != day and L <= abs(Map[nx][ny]-Map[x][y]) <= R:
                    visited[nx][ny] = day
                    people += Map[nx][ny]
                    union.append([nx,ny])
                    Q.append([nx,ny])
    if len(union) > 1:
        people //= len(union)
        for coord in union:
            Map[coord[0]][coord[1]] = people
            coords.appendleft(coord)
        return True
    return False


coords = deque()
for x in range(N):
    for y in range(N):
        coords.appendleft([x,y])
visited = [[-1]*N for _ in range(N)]
day = 0
while True:
    flag = True
    for _ in range(len(coords)):
        x,y = coords.pop()
        if visited[x][y] != day:
            if getunion(x,y):
                flag = False

    if flag:
        break
    day += 1

print(day)