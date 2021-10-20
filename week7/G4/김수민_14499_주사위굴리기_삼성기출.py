# BOJ 14499 주사위 굴리기[삼성 SW 역량 테스트 기출] 골드4 - 김수민
from collections import deque
N, M, y, x, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
dice_garo = deque([0, 0, 0, 0]) # 주사위 전개도 가로 부분
dice_sero = deque([0, 0, 0, 0]) # 주사위 전개도 세로 부분분Q = deque()
order = list(map(int, input().split()))
top = 0
for k in range(K):
    dir = order[k]
    ny = y + dy[dir - 1]
    nx = x + dx[dir - 1]
    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        continue
    y, x = ny, nx
    # 동,서,남,북일 경우 주사위 전개도 변화
    if dir == 1:
        a = dice_garo.pop()
        dice_garo.appendleft(a)
    elif dir == 2:
        a = dice_garo.popleft()
        dice_garo.append(a)
    elif dir == 3:
        a = dice_sero.popleft()
        dice_sero.append(a)
    else:
        a = dice_sero.pop()
        dice_sero.appendleft(a)
    # 가로와 세로가 공유하는 주사위 위, 바닥 동기화
    if dir == 1 or dir == 2:
        top, bottom = dice_garo[1], dice_garo[3]
        dice_sero[1], dice_sero[3] = top, bottom
    else:
        top, bottom = dice_sero[1], dice_sero[3]
        dice_garo[1], dice_garo[3] = top, bottom
    # 지도가 0일 경우와 0이 아닐 경우
    if MAP[ny][nx] == 0:
        MAP[ny][nx] = bottom
    else:
        bottom = MAP[ny][nx]
        MAP[ny][nx] = 0
        dice_garo[3], dice_sero[3] = bottom, bottom
    print(top)

