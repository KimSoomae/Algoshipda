import sys; sys.stdin = open('14500_테트로미노_G5.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
tetro = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 1)]]

def tetro1(row, col):
    # (r, c), (c, r)
    routes = [(0, 1), (0, 2), (0, 3)]
    tmp = [board[row][col]] * 2
    result = 0
    for i in range(2):
        for route in routes:
            nr = row + route[i % 2]
            nc = col + route[(i + 1) % 2]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                tmp[i] = 0
                break
            tmp[i] += board[nr][nc]
    return max(tmp)

def tetro2(row, col):
    # only 1
    route = [(0, 1), (1, 0), (1, 1)]
    tmp = board[row][col]
    for r, c in route:
        if row + r < 0 or row + r >= N or col + c < 0 or col + c >= M:
            tmp = 0
            break
        tmp += board[row + r][col + c]
    return tmp

def tetro3(row, col):
    # all
    routes = [(1, 0), (2, 0), (2, 1)]
    point = [(1, 1), (1, 1), (-1, 1), (-1, 1), (1, -1), (1, -1), (-1, -1), (-1, -1)]
    tmp = [board[row][col]] * 8
    for i in range(8):
        for route in routes:
            nr = row + (route[i % 2] * point[i][0])
            nc = col + (route[(i + 1) % 2] * point[i][1])
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                tmp[i] = 0
                break
            tmp[i] += board[nr][nc]
    return max(tmp)

def tetro4(row, col):
    # (r, c), (c, r), (r, -c), (-c, r)
    routes = [(1, 0), (1, 1), (2, 1)]
    point = [(1, 1), (1, 1), (1, -1), (-1, 1)]
    tmp = [board[row][col]] * 4
    for i in range(4):
        for route in routes:
            nr = row + (route[i % 2] * point[i][0])
            nc = col + (route[(i + 1) % 2] * point[i][1])
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                tmp[i] = 0
                break
            tmp[i] += board[nr][nc]
    return max(tmp)

def tetro5(row, col):
    # (r, c), (c, r), (-r, c), (c, -r)
    routes = [(0, 1), (0, 2), (1, 1)]
    point = [(1, 1), (1, 1), (-1, 1), (1, -1)]
    tmp = [board[row][col]] * 4
    for i in range(4):
        for route in routes:
            nr = row + (route[i % 2] * point[i][0])
            nc = col + (route[(i + 1) % 2] * point[i][1])
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                tmp[i] = 0
                break
            tmp[i] += board[nr][nc]
    return max(tmp)

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, tetro1(i, j), tetro2(i, j), tetro3(i, j), tetro4(i, j), tetro5(i, j))

print(result)
