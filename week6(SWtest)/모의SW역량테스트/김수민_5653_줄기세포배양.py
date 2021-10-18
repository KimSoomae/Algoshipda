# 5653 [모의 SW 역량테스트] 줄기세포배양 - 김수민
from collections import deque
import heapq
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs():
    global anw
    dead = deque()
    # 주어진 시간 동안
    for time in range(K + 1):
        # 비활성화인 세포들 활성화될떄 까지 시간 -1
        for w in range(len(wait)):
            y, x, cnt = wait.popleft()
            if cnt >= 0:
                cnt -= 1
                wait.append((y, x, cnt))
            # 활성화 할떄가 됐으면 (번지는 시간 1시간이니까 그냥 1시간 후에 활성화됨과 동시에 번진다고 생각
            elif cnt == -1:
                # 동시에 번지려고 하면 더 높은 생명력인 세포가 번지므로, 생명력을 우선순위로 하는 최대힙에 저장
                heapq.heappush(active, (-julgi[y][x], (y, x, julgi[y][x])))
        while active:
            w, ww = heapq.heappop(active)
            y, x, life = ww
            # 상하좌우에 세포가 없으면 번식하고 비활성화 목록에 추가. 정답 카운트도 + 1
            for idx in range(4):
                ny = y + dy[idx]
                nx = x + dx[idx]
                if julgi[ny][nx] > 0 or julgi[ny][nx] == -2:
                    continue
                julgi[ny][nx] = life
                anw += 1
                # 번식하고 한시간 후에 for문 돌면 1시간 지나므로 생명력 -1해서 넣어준다
                wait.append((ny,nx,julgi[ny][nx]-1))
            # 퍼뜨린 세포는 죽음 큐에 추가
            dead.append((y, x, life))
        n = len(dead)
        for k in range(n):
            y, x, dead_life = dead.popleft()
            # 생명력 1이었으면 바로 죽으니까 죽이고, 정답 카운트 -1
            if dead_life == 1:
                julgi[y][x] = -2
                anw -= 1
            # 생명력 1이상이었으면 바로 안죽으니까 생명력 -1해서 다시 죽음 큐에 저장하고 다음 time때 점검
            else:
                dead_life -= 1
                dead.append((y, x, dead_life))


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 전체 배열 선언
    julgi = [[0] * 1000 for _ in range(1000)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    wait = deque() # 비활성화 상태인 세포들
    active = [] # 활성화 상태인 세포들
    anw = 0
    for i in range(N):
        for j in range(M):
            # 전체 배열에 주어진 세포들 저장(가운데에)
            julgi[500-(N//2) + i][500-(M // 2) + j] = arr[i][j]
            if arr[i][j] != 0:
                anw += 1 # 세포 있으면 비활성화 목록에 추가, 정답 카운트도 +1
                wait.append((500-(N // 2) + i, 500-(M//2) + j, arr[i][j]))
    bfs()
    print(f'#{tc} {anw}')

