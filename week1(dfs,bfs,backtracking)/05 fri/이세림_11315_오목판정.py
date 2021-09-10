import sys
sys.stdin = open('11315.txt')

def check(x, y):
    for i in range(8):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 'o':
            cnt += 1
            nx = nx + dx[i]
            ny = ny + dy[i]
        if cnt >= 5:
            return True
    return False

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

for case in range(1, int(input())+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if data[i][j] == 'o':
                if check(i, j):
                    result = 'YES'
                    break
        if result == 'YES':
            break
    print('#{} {}'.format(case, result))