from collections import deque


def bfs(si, sj):
    cnt = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = deque([(si,sj)]) # 리스트 안에 넣어줘야 함!
    visited[si][sj] = True
    while q:
        i, j = q.popleft()
        cnt += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if house[ni][nj] == 1 and visited[ni][nj] == False:
                    q.append((ni,nj))
                    visited[ni][nj] = True
    ans.append(cnt)


n = int(input())
house = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
total = 0
ans = []
for si in range(n):
    for sj in range(n):
        if house[si][sj] == 1 and visited[si][sj] == False:
            total += 1
            bfs(si, sj)

ans.sort()
print(total)
for i in ans:
    print(i)