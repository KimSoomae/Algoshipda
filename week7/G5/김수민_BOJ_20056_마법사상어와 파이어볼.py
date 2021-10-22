# 22056 마법사 상어와 파이어볼 [삼성SW역량테스트 기출- 구현] 골드5 - 김수민
from collections import deque
N, M, K = map(int, input().split())
Q = deque(); cnt = 0
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(M):
    y, x, m, s, d = map(int, input().split())
    Q.append((y - 1, x - 1, m, s, d))

anw = 0
while cnt < K:
    bomblist = deque()
    arr = [[[] for _ in range(N)] for _ in range(N)]
    visit = [[1] * N for _ in range(N)]
    hubo = []
    while Q:
        y, x, m, s, d = Q.popleft()
        ny = y + dy[d] * s; nx = x + dx[d] * s
        # 방향 조정(경계 넘어가면)
        if ny >= N:
            ny = ny % N
        elif ny < 0:
            while ny < 0:
                ny = N + ny
        if nx >= N:
            nx = nx % N
        elif nx < 0:
            while nx < 0:
                nx = N + nx
        if arr[ny][nx]:
            yy, xx, mm, ss, dd = arr[ny][nx].pop()
            mm += m; ss += s
            if (dd % 2 and d % 2 == 0) or (dd % 2==0 and d % 2 == 1):
                dd = -1
            arr[ny][nx].append((yy,xx,mm,ss,dd))
            visit[ny][nx] += 1
            if visit[ny][nx] <= 2:
                bomblist.append((ny, nx))
        else:
            hubo.append((ny, nx, m, s, d))
            arr[ny][nx].append((ny, nx, m, s, d))
    for idx in range(len(hubo)):
        y, x, m, s, d = hubo[idx]
        if visit[y][x] == 1:
            Q.append((y, x, m, s, d))
    for idx in range(len(bomblist)):
        r, c = bomblist.popleft()
        y, x, totm, tots, d = arr[r][c].pop()
        if totm//5 == 0:
            continue
        if d != -1:
            for p in range(4):
                Q.append((r, c, totm//5, tots//visit[r][c], p * 2))
        else:
            for p in range(4):
                Q.append((r, c, totm//5, tots//visit[r][c], p * 2 + 1))
    cnt += 1

anw = 0
for i in range(len(Q)):
    y, x, m, s, d = Q[i]
    anw += m

print(anw)



