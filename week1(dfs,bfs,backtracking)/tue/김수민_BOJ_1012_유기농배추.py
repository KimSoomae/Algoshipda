def bfs(x, y):
    visited[x][y] = 1
    q.append([x, y])
    while len(q) != 0:
        now = q.pop(0)
        x = now[0]
        y = now[1]
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx>=0 and newx<N and newy >=0 and newy< M and bechu[newx][newy] == 1 and visited[newx][newy]==0:
                visited[newx][newy] = 1
                q.append([newx, newy])


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    bechu = [[0]*M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    anw = 0
    for i in range(K):
        a, b = map(int, input().split())
        bechu[b][a] = 1
    for i in range(N):
        for j in range(M):
            if visited[i][j]==0 and bechu[i][j] == 1:
                bfs(i, j)
                anw += 1
    print(anw)