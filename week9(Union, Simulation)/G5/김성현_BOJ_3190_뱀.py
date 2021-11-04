input = open('input.txt').readline
from collections import deque

N = int(input().strip())
apple_N = int(input())

apple = []
for _ in range(apple_N):
    app_c, app_r = tuple(map(int, input().strip().split()))
    app_c -=1; app_r -=1
    apple.append((app_c, app_r))

L = int(input().strip())
direct = [tuple(input().strip().split()) for _ in range(L)]
now_direct = []
dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1] 


def go_onestep(snake, i):
    hc, hr = snake[0]
    
    (new_c, new_r) = (hc + dc[i], hr + dr[i])
    if (new_c, new_r) in snake:
        return False

    if (new_c, new_r) in apple:
        snake.appendleft((new_c, new_r))
    else:
        snake.appendleft((new_c, new_r))
        snake.pop()

    
    if 0 <= new_c <= N-1 and 0 <= new_r <= N-1:
        return True
    else:
        return False
    
def turn(ch):
    global i
    if ch =='D':
        i = (i+1) % 4
    else:
        i = (i-1) % 4
snake = deque()
snake.append((0, 0))
i =  1

cnt = 0
while True:
    if not now_direct:
        if direct:
            now_direct.append(direct.pop(0))
            time, D = now_direct[0]
            time = int(time)

    cnt += 1
    result = go_onestep(snake, i)
    
    if result == False:
        print(cnt)
        break
    
    if cnt == time:
        turn(D)
        now_direct.pop()











