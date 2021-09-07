from collections import deque


def bfs(start_i, start_j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited[start_i][start_j] = True
    q = deque([(start_i, start_j)])
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if field[ni][nj] == 1 and visited[ni][nj] == False:
                    q.append((ni, nj))
                    visited[ni][nj] = True


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    for si in range(N):
        for sj in range(M):
            if field[si][sj] == 1 and visited[si][sj] == False:
                cnt += 1
                bfs(si, sj)
    print(cnt)
