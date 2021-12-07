from collections import deque
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
s = []
def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit = [[0] * m for i in range(n)]
    visit[i][j] = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and temp[x][y] != 0:
                temp[x][y] = 0
                visit[x][y] = 1
                q.append([x, y])
def check(i, j):
    cnt = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < m and t[x][y] == 0:
            cnt += 1
    return cnt
def checkz():
    for i in range(n):
        for j in range(m):
            if s[i][j] != 0:
                return False
    return True
for i in range(n):
    s.append(list(map(int, input().split())))
result = 1
while True:
    if checkz():
        print(0)
        break
    t = copy.deepcopy(s)
    for i in range(n):
        for j in range(m):
            if t[i][j] != 0:
                temp = s[i][j] - check(i, j)
                s[i][j] = temp if temp >= 0 else 0
    temp = copy.deepcopy(s)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] != 0:
                temp[i][j] = 0
                bfs(i, j)
                cnt += 1
    if cnt > 1:
        print(result)
        break
    result += 1