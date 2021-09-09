def bfs(y, x, visit_V):
    visited[y][x] = visit_V
    q.append([y, x])
    dis = 0
    global anw
    while q:
        dis += 1
        for _ in range(len(q)):
            now = q.pop(0)
            y = now[0]
            x = now[1]
            for i in range(4):
                newx = x + dx[i]
                newy = y + dy[i]
                if newx < 0 or newx >= M or newy < 0 or newy >= N:
                    continue
                if arr[newy][newx] == 'W' or visited[newy][newx] >= visit_V:
                    continue
                visited[newy][newx] = visit_V
                q.append([newy,newx])
    dis -= 1
    if anw < dis:
        anw = dis


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = []
anw = 0
visited = [[0] * M for _ in range(N)]
visit_V = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visit_V += 1
            bfs(i, j, visit_V)
print(anw)
