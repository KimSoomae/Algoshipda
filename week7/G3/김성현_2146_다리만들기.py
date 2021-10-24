input = open('input.txt').readline
from collections import deque
N = int(input())

dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

def bfs(c, r):

    beach = []

    Q = deque()
    Q.append((c, r))
    visited = [[0] * N for _ in range(N)]
    while Q:
        c, r = Q.pop()
        visited[c][r] = 1

        for i in range(4):
            new_c = c + dc[i]
            new_r = r + dr[i]

            if 0 <= new_c <= N-1 and 0 <= new_r <= N-1:
                if board[new_c][new_r] and not visited[new_c][new_r]:
                    Q.append((new_c, new_r))
                else:
                    if not (new_c, new_r) in beach and board[new_c][new_r] == 0:
                        beach.append((new_c, new_r))
    return beach, visited

def bfs2(c, r, territory):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append((c, r))
    reached = False
    while Q:
        
        temp = []
        while Q:
            c, r = Q.pop()
            visited[c][r] = 1
            for i in range(4):
                new_c = c + dc[i]
                new_r = r + dr[i]

                if 0 <= new_c <= N-1 and 0 <= new_r <= N-1:
                    if board[new_c][new_r] == 0 and not visited[new_c][new_r]:
                        temp.append((new_c, new_r))
                    else:
                        if board[new_c][new_r] and (not (new_c, new_r) in territory):
                            reached = True
                            break
        if reached:
            return cnt
        else:
            cnt += 1

        for x in temp:
            Q.append(x)
        
        
    


board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


conti = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j]:
            beach_locations, territory = bfs(i, j)
            conti.append([beach_locations, territory])

min_val = 0xffffff
for beach in conti:
    for c, r in beach[0]:
        min_val = min(min_val, bfs2(c, r, beach[1]))

print(min_val)

            

