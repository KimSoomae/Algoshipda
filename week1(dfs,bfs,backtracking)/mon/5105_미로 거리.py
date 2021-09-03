def BFS(x, y):
    global anw
    Q = []
    visit = [[0] * (N + 1) for _ in range(N)]
    Q.append([x, y])
    visit[x][y] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while Q:
        v = Q.pop(0)
        tmpx = v[0]
        tmpy = v[1]
        for i in range(4):
            newx = tmpx + dx[i]
            newy = tmpy + dy[i]
            if newx >= 0 and newx < N and newy >= 0 and newy < N and G[newx][newy] != 1 and visit[newx][newy] == 0:
                visit[newx][newy] = visit[tmpx][tmpy] + 1
                if G[newx][newy] == 0:
                    Q.append([newx, newy])
                elif G[newx][newy] == 3:
                    if visit[newx][newy] < anw:
                        anw = visit[newx][newy]
    if anw == 1000000: return 0
    return anw - 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    G = []
    start = [0, 0];
    end = [0, 0]
    anw = 1000000
    for i in range(N):
        G.append(list(map(int, input())))
    for i in range(N):
        for j in range(N):
            if G[i][j] == 2:
                start[0] = i;
                start[1] = j
    print(f'#{tc} {BFS(start[0], start[1])}')