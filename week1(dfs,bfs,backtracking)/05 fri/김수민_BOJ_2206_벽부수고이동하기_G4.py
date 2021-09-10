def bfs(y, x):
    global anw
    flag = False
    q.append([y, x, 0])
    visited[y][x][0] = 1
    while len(q):
        now = q.pop(0)
        y = now[0]
        x = now[1]
        wall = now[2]
        if y == N - 1 and x == M - 1:
            flag = True
            anw = visited[y][x][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if m[ny][nx] == 0 and visited[ny][nx][wall] == 0:
                visited[ny][nx][wall] = visited[y][x][wall] + 1
                q.append([ny, nx, wall])
            elif m[ny][nx] == 1 and wall == 0:
                visited[ny][nx][1] = visited[y][x][0] + 1
                q.append([ny, nx, wall + 1])
    if flag == False:
        anw = -1




N, M = map(int, input().split())
m = [list(map(int, input())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = []
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
# visited[y좌표, x좌표, 0] = 벽부수기 안썼을 때
# visited[y좌표, x좌표, 1] = 벽부수기 썼을 때
anw = 10000000
bfs(0, 0)
print(anw)