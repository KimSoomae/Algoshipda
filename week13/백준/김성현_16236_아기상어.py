input = open('input.txt').readline
from collections import deque
N = int(input())

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
board = [list(map(int, input().split())) for _ in range(N)]
shark_c = 0; shark_r = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_c = i
            shark_r = j
            break
    if shark_c or shark_r:
        break

size = 2
now_eat = 0
total_time = 0
def bfs(shark_c, shark_r, size, now_eat, total_time):
    possible = True
    visited = [[0] * N for _ in range(N)]
    visited[shark_c][shark_r] = 1

    eat_able = []
    distance = 0
    

    q = deque()
    q.append((shark_c, shark_r))

    while q:
        distance += 1
        for _ in range(len(q)):
            c, r = q.popleft()

            for i in range(4):
                nc = c + dc[i]
                nr = r + dr[i]

                if 0 <= nc < N and 0 <= nr < N:
                    if not visited[nc][nr]: 
                        visited[nc][nr] = 1

                        if not board[nc][nr]:
                            q.append((nc, nr))

                        if board[nc][nr] > size:
                            pass

                        if board[nc][nr] == size:
                            q.append((nc, nr))
                        
                        if board[nc][nr] < size and board[nc][nr]:
                            eat_able.append((nc, nr))
        if eat_able:
            break
    if not eat_able:
        possible = False
        return shark_c, shark_r, size, now_eat, total_time, possible
    
    total_time += distance
    eat_able.sort(key = lambda x: x[0])

    temp = []

    for fish in eat_able:
        if not temp:
            temp.append(fish)
        elif fish[0] > temp[0][0]:
            break    
        else:
            temp.append(fish)
    
    temp.sort(key = lambda x: x[1])
    tc, tr = temp[0]

    board[tc][tr] = 9
    board[shark_c][shark_r] = 0

    shark_c = tc; shark_r = tr

    now_eat += 1
    if size == now_eat:
        size += 1
        now_eat = 0
    return shark_c, shark_r, size, now_eat, total_time, possible



while True:
    now_time = 0
    shark_c, shark_r, size, now_eat, time, possible = bfs(shark_c, shark_r, size, now_eat, now_time)

    total_time += time
    if not possible:
        break

print(total_time)


    