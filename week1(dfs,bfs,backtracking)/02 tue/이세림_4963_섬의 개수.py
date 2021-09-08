import sys
sys.stdin = open('4963.txt', 'r')

def dfs(x, y):
    graph[x][y] = 0
    for k in range(len(r)):
        X = x + r[k]
        Y = y + c[k]
        if (0 <= X < h) and (0 <= Y < w) and graph[X][Y] == 1:
            dfs(X, Y)

while True:
    w, h = map(int, input().split())
    if w == h == 0:  # 마지막 0 0 입력을 받으면 종료
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    r = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우, 대각선
    c = [0, 0, -1, 1, -1, 1, -1, 1]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
