# BOJ 21610 마법사 상어와 비바라기[삼성Sw역량테스트 기출, 구현] - 골드5 김수민
from collections import deque
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = deque()
cloud.append((N-2, 0))
cloud.append((N-2, 1))
cloud.append((N-1,0))
cloud.append((N-1,1))
for k in range(M):
    d, s = map(int, input().split())
    visit = [[0] * N for _ in range(N)]
    # 구름 이동
    for ss in range(len(cloud)):
        y, x = cloud.popleft()
        ny, nx = y + dy[d] * s, x + dx[d] * s
        # 경계 벗어났을 때 연결
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
        cloud.append((ny, nx))
        visit[ny][nx] = 1
        # 비 내리기
        arr[ny][nx] += 1
    # 물복사버그 마법(대각선에 구름 있으면 1씩 증가)
    for ss in range(len(cloud)):
        ny, nx = cloud[ss]
        for j in range(2, 9, 2):
            new_ny, new_nx = ny + dy[j], nx + dx[j]
            if new_ny < 0 or new_ny >= N or new_nx < 0 or new_nx >= N: continue
            if arr[new_ny][new_nx] > 0:
                arr[ny][nx] += 1
    # 비내리기 끝. 이제 2이상인 칸에 구름 생성
    new_cloud = deque()
    for iii in range(N):
        for jjj in range(N):
            if arr[iii][jjj] >= 2 and visit[iii][jjj] == 0:
                new_cloud.append((iii, jjj))
                arr[iii][jjj] -= 2
    cloud = new_cloud
anw = 0
for i in range(N):
    for j in range(N):
        anw += arr[i][j]
print(anw)
