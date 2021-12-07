input = open('input.txt').readline
from collections import deque
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
for i in range(M):
    for j in range(N):
        if board[j][i] == 1:
            Q.append((j, i))

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

cnt = 0
while Q:
    temp = []
    while Q:
        c, r = Q.popleft()
        for i in range(4):
            new_c = c + dc[i]
            new_r = r + dr[i]

            if 0 <= new_c <= N-1 and 0 <= new_r <= M-1:
                if not board[new_c][new_r]:
                    board[new_c][new_r] = 1
                    temp.append((new_c, new_r))

    
    for tup in temp:
        Q.append(tup)
    cnt += 1

not_complete = False
for i in range(M):
    for j in range(N):
        if board[j][i] == 0:
            not_complete = True

if not_complete:
    print(-1)
else:
    print(cnt-1)





