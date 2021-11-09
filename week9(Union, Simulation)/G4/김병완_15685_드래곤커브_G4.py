import sys; sys.stdin = open('15685_드래곤커브_G4.txt', 'r')
input = sys.stdin.readline

def draw_curve(r, c, direc, gth):
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    tmp = []
    tmp.append((r, c))
    board[r][c] = 1
    nr = r + dr[direc]
    nc = c + dc[direc]
    tmp.append((nr, nc))
    board[nr][nc] = 1

    cnt = 0
    while cnt < gth:
        cnt += 1
        piv_r, piv_c = tmp[-1]
        for i in range(len(tmp) - 2, -1, -1):
            row, col = tmp[i]
            b = row - piv_r
            a = col - piv_c
            if a > 0 and b == 0:
                if piv_r + a < 0 or piv_r + a >= 101 or piv_c < 0 or piv_c >= 101: continue
                tmp.append((piv_r + a, piv_c))
                board[piv_r + a][piv_c] = 1
                continue
            elif a == 0 and b > 0:
                if piv_r < 0 or piv_r >= 101 or piv_c - b < 0 or piv_c - b >= 101: continue
                tmp.append((piv_r, piv_c - b))
                board[piv_r][piv_c - b] = 1
                continue
            elif a < 0 and b == 0:
                if piv_r + a < 0 or piv_r + a >= 101 or piv_c < 0 or piv_c >= 101: continue
                tmp.append((piv_r + a, piv_c))
                board[piv_r + a][piv_c] = 1
                continue
            elif a == 0 and b < 0:
                if piv_r < 0 or piv_r >= 101 or piv_c - b < 0 or piv_c - b >= 101: continue
                tmp.append((piv_r, piv_c - b))
                board[piv_r][piv_c - b] = 1
                continue

            if a < 0 and b < 0:
                na = abs(b)
                nb = abs(a) * (-1)
                nc = piv_c + na
                nr = piv_r + nb
                if nc < 0 or nc >= 101 or nr < 0 or nr >= 101: continue
                tmp.append((nr, nc))
                board[nr][nc] = 1
            elif a > 0 and b < 0:
                na = abs(b)
                nb = abs(a)
                nc = piv_c + na
                nr = piv_r + nb
                if nc < 0 or nc >= 101 or nr < 0 or nr >= 101: continue
                tmp.append((nr, nc))
                board[nr][nc] = 1
            elif a > 0 and b > 0:
                na = abs(b) * (-1)
                nb = abs(a)
                nc = piv_c + na
                nr = piv_r + nb
                if nc < 0 or nc >= 101 or nr < 0 or nr >= 101: continue
                tmp.append((nr, nc))
                board[nr][nc] = 1
            elif a < 0 and b > 0:
                na = abs(b) * (-1)
                nb = abs(a) * (-1)
                nc = piv_c + na
                nr = piv_r + nb
                if nc < 0 or nc >= 101 or nr < 0 or nr >= 101: continue
                tmp.append((nr, nc))
                board[nr][nc] = 1
    # print(tmp)


N = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(N):
    c, r, d, g = map(int, input().split())
    draw_curve(r, c, d, g)

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            result += 1

print(result)
