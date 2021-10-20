# BOJ 20057 마법사 상어와 토네이도[삼성 SW 역량 테스트 기출] 골드 3 - 김수민
import math
def find(dir, y, x):
    blowed = 0
    global anw
    y, x = y + dy[dir], x + dx[dir]
    original = arr[y][x]
    for j in range(10):
        ny, nx = y + dusty[dir][j], x + dustx[dir][j]
        # 경계 밖으로 벗어난 모래 anw에 추가
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            if j == 9:
                anw += (original - blowed)
            else:
                anw += math.floor(arr[y][x] * blow[j])
                blowed += math.floor(arr[y][x] * blow[j])
            continue
        # 경계 안으로 들어오면 해당 위치에 흩날린 만큼 모래 더해주고, 마지막에 남은 모래들 알파 칸으로 보내기 위해 지금까지 흩날린 모래도 계산
        arr[ny][nx] += math.floor(arr[y][x] * blow[j])
        blowed += math.floor(arr[y][x] * blow[j])
        # 알파 칸으로 보내기
        if j == 9:
            arr[ny][nx] += (original - blowed)
            arr[y][x] = 0
    return y, x
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
# 흩날리는 모래의 동서남북 이동 인덱스
dusty = [[0, -1, 1, -2, -1, 1, 2, -1, 1, 0], [2, 1, 1, 0, 0, 0, 0, -1, -1, 1], [0, -1, 1, -2, -1, 1, 2, -1, 1, 0], [-2, -1, -1, 0, 0, 0, 0, 1, 1, -1]]
dustx = [[-2, -1, -1, 0, 0, 0, 0, 1, 1, -1], [0, -1, 1, -2, -1, 1, 2, -1, 1, 0], [2, 1, 1, 0, 0, 0, 0, -1, -1, 1], [0, -1, 1, -2, -1, 1, 2, -1, 1, 0]]
# 흩날리는 모래의 인덱스에 해당하는 비율
blow = [0.05, 0.1, 0.1, 0.02, 0.07, 0.07, 0.02, 0.01, 0.01, 0]
idx = 1
y, x = N//2, N//2
anw = 0
flag = False
while idx <= N:
    for i in range(idx):
        y,x = find(0, y, x)
        if y == 0 and x == 0: # 토네이도 끝
            flag = True
            break
    if flag:
        break
    for i in range(idx):
        # 남쪽으로 바람불기
        y, x = find(1, y, x)
    idx += 1
    for i in range(idx):
        # 동쪽으로 바람부기
        y, x= find(2, y, x)
    for i in range(idx):
        # 북쪽으로 바람불기
        y,x = find(3, y, x)
    idx += 1
print(anw)