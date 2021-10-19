# BOJ 3190 뱀 [삼성 SW 역량 테스트 기출] - 김수민 (40분)
from collections import deque
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs():
    while tmp:
        y, x, time, dir = tmp.popleft()
        ny = y + dy[dir]
        nx = x + dx[dir]
        # 벽에 부딪히거나 새로 이동할 곳에 자기 몸이 있으면 걸린 시간 리턴(이동 예정인 좌표니까 시간 + 1 해줌)
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            return time + 1
        if ((ny, nx)) in snake:
            return time + 1
        # 방향이동시간이면 방향 바꿔준다. dy, dx가 시계방향 순서이므로 왼,오에 따라 인덱스 조절
        if Q:
            if time + 1 == int(Q[0][0]):
                t, d = Q.popleft()
                if d == 'D':
                    dir = (dir + 1) % 4
                elif d == 'L':
                    dir = (dir + 3) % 4
        snake.append((ny, nx))  # 뱀
        if arr[ny][nx] != 1:  # 사과 없으면
            snake.popleft()  # 꼬리떼기
        elif arr[ny][nx] == 1: # 사과 먹으면
            arr[ny][nx] = 0 # 사과부분 0으로
        tmp.append((ny, nx, time + 1, dir))

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for k in range(K):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1
Q = deque() # 방향 전환
tmp = deque() # 새로 이동할 뱀의 머리 부분 (y좌표, x좌표, 시간, 방향) 담음
snake = deque() # 뱀의 몸에 해당되는 좌표 담음
L = int(input())
snake.append((0,0))

for l in range(L):
    t, dir = input().split()
    Q.append((t, dir))

tmp.append((0,0,0,0))
print(bfs())
