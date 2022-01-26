input = open('input.txt').readline
from pprint import pprint


def move(dir, s): 
    new_clouds = [[0] * N for _ in range(N)]

    for c in range(N):
        for r in range(N):
            if clouds[c][r]:
                nc = (c + dc[dir]*s) % N
                nr = (r + dr[dir]*s) % N
                new_clouds[nc][nr] = 1
    return new_clouds

def duplicate(c, r):
    cnt = 0
    for i in (2, 4, 6, 8):
        nc = (c + dc[i])
        nr = (r + dr[i])

        if 0 <= nc < N and 0 <= nr < N:
            if board[nc][nr]:
                cnt += 1

    board[c][r] += cnt



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order_list = []
for _ in range(M):
    order_list.append(list(map(int, input().split())))

dc = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]

clouds = [[0] * N for _ in range(N)]
clouds[N-1][0] = clouds[N-1][1] = clouds[N-2][0] = clouds[N-2][1] = 1

for i in range(M):
    dir, s = order_list[i]
    clouds = move(dir, s) #1. 이동

    for c in range(N): 
        for r in range(N):
            if clouds[c][r]:
                board[c][r] += 1 #2. 물+1
                clouds[c][r] = 2 #3. 구름제거

    for c in range(N):
        for r in range(N):
            if clouds[c][r] == 2: #4. 물복사버그
                duplicate(c, r)
  
    for c in range(N):
        for r in range(N):
            if clouds[c][r] == 2:
                clouds[c][r] = 0
            else:
                if board[c][r] >= 2:
                    board[c][r] -= 2
                    clouds[c][r] = 1

result = 0
for c in range(N):
    for r in range(N):
        result += board[c][r]

print(result)