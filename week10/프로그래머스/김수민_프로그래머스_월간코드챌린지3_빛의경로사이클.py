import sys
sys.setrecursionlimit(1000000) # 재귀함수 제한 늘리기
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = []

# 범위 넘어가면 반대쪽 끝으로 돌아오기
def check(n, l):
    if n >= l:
        n %= l
    elif n < 0:
        while n < 0:
            n = l + n
    return n
# 순환
def dfs(y, x, dr, garo, sero, cnt, grid, visit):
    # 경로 사이클 형성 됐으면
    if visit[dr][y][x]:
        answer.append(cnt)
        return
    elif visit[dr][y][x] == 0:
        visit[dr][y][x] = 1
        # 우회전
        if grid[y][x] == "R":
            dr = (dr + 1) % 4
        # 좌회전
        elif grid[y][x] == "L":
            if dr - 1 < 0:
                dr = 3
            else:
                dr -= 1
        ny = y + dy[dr]
        nx = x + dx[dr]
        if ny < 0 or ny >= sero: ny = check(ny, sero)
        if nx < 0 or nx >= garo: nx = check(nx, garo)
        dfs(ny, nx, dr, garo, sero, cnt + 1, grid, visit)

def solution(grid):
    sero = len(grid)
    garo = len(grid[0])
    # visit[방향][세로축][가로축]
    visit = [[[0 for k in range(garo)] for j in range(sero)] for i in range(4)]
    for i in range(sero):
        for j in range(garo):
            for k in range(4):
                if visit[k][i][j]: continue
                dfs(i, j, k, garo, sero, 0, grid, visit)
    answer.sort()
    return answer