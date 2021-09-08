def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1
    global flag
    while len(q) != 0:
        now = q.pop(0)
        x = now[0]
        y = now[1]
        for i in range(8):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx>=0 and newx<N and newy >=0 and newy<M:
                if mount[newx][newy] > mount[x][y]:
                    flag = False
                if mount[newx][newy] == mount[x][y] and visited[newx][newy]==0:
                    visited[newx][newy] = 1
                    q.append([newx, newy])


N, M = map(int, input().split())
mount = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = []
dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]
anw = 0
for i in range(N):
    for j in range(M):
        if mount[i][j] != 0 and visited[i][j] == 0:
            # 산봉우리 확인 여부
            flag = True
            bfs(i, j)
            if flag == True:
                anw += 1
print(anw)