def find():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    tmpq = []
    tmparr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmparr[i][j] = arr[i][j]
    for k in range(len(q)):
        tmpq.append([q[k][0],q[k][1]])
    cnt = 0
    global result
    while len(tmpq):
        now = tmpq.pop(0)
        y = now[0]
        x = now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                if tmparr[ny][nx] == 0:
                    tmparr[ny][nx] = 2
                    tmpq.append([ny, nx])
    for i in range(N):
        for j in range(M):
            if tmparr[i][j] == 0:
                cnt += 1
    if cnt > result:
        result = cnt



def dfs(cnt):
    global result
    if cnt == 0:
        find()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(cnt - 1)
                arr[i][j] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            q.append([i, j])
dfs(3)
print(result)