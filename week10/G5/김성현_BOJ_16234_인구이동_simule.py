input = open('input.txt').readline
from collections import deque

def bfs(c, r):
    result = [(c, r)]

    Q = deque()
    Q.append((c, r))
    value = board[c][r]
    cnt = 1

    while Q:
        c, r = Q.popleft()
        
        visited[c][r] = 1

        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc <= N-1 and 0 <= nr <= N-1 and not visited[nc][nr]:
                if L <= abs(board[c][r] - board[nc][nr]) <= R:
                    Q.append((nc, nr))
                    if not (nc, nr) in result:
                        result.append((nc, nr))
                        value += board[nc][nr]
                        cnt += 1

    if len(result) != 1:
        return result, value//cnt
    else:
        return 0, 0
        


def calculate(Ulist):
    while Ulist:
        union, value = Ulist.pop()
               
        for c, r in union:
            board[c][r] = value

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]


cnt = 0
while True:
    visited = [[0]*N for _ in range(N)]
    union_list = []

    for c in range(N):
        for r in range(N):
            if not visited[c][r]: 
                union, value = bfs(c, r)
                if union:
                    union_list.append((union, value))

    if not union_list:
        break

    calculate(union_list)
    cnt += 1

print(cnt)


#code 2

from collections import deque
def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(s[nx][ny] - s[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
while True:
    visit = [[0] * n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum([s[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        s[x][y] = num
    if not isTrue:
        break
    cnt += 1
print(cnt)