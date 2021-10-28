from collections import deque
#from pprint import pprint

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs1(si, sj):
    global cnt
    q = deque()
    q.append((si, sj))
    visit[si][sj] = True
    arr[si][sj] = cnt

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 1 and not visit[ni][nj]:
                    visit[ni][nj] = True
                    arr[ni][nj] = cnt
                    q.append((ni, nj))


def bfs2(z):
    global answer
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for find_i in range(n):
        for find_j in range(n):
            if arr[find_i][find_j] == z:
                q.append((find_i, find_j))
                dist[find_i][find_j] = 0

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue

            if arr[ni][nj] > 0 and arr[ni][nj] != z:
                answer = min(answer, dist[i][j])
                return

            if arr[ni][nj] == 0 and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
cnt = 1
answer = 987654321

for si in range(n):
    for sj in range(n):
        if not visit[si][sj] and arr[si][sj] == 1:
            bfs1(si, sj)
            cnt += 1

#pprint(arr)

for x in range(1, cnt):
    bfs2(x)

print(answer)