import sys; readline = sys.stdin.readline
from collections import deque

Map = [readline().rstrip() for _ in range(5)]
S_loc = []
for x in range(5):
    for y in range(5):
        if Map[x][y] == 'S':
            S_loc.append([x,y])

anw = 0
visited = [[True]*5 for _ in range(5)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

query_set = set()

def dfs(i,Y):
    global anw
    if Y >= 4:
        return
    if i == 7:
        anw += 1
        query_set.add(tuple(sorted(stack)))
        return
    safe = set()
    for x,y in stack:
        for _ in range(4):
            if 5 > x+dx[_] >= 0 and 5 > y+dy[_] >= 0 and visited[x+dx[_]][y+dy[_]]:
                safe.add((x+dx[_],y+dy[_]))

    for x,y in safe:
        if x<0 or x>=5 or y<0 or y>=5 or not visited[x][y]:
            continue

        stack.append((x,y))
        visited[x][y] = False
        if Map[x][y] == 'S':
            dfs(i+1,Y)
        else:
            dfs(i+1,Y+1)
        visited[x][y] = True
        stack.pop()


stack = deque([])
for x,y in S_loc:
    stack.append((x,y))
    visited[x][y] = False
    dfs(1,0)
    stack.pop()

print(len(query_set))
print(anw)