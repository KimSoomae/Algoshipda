input = open('input.txt').readline
from pprint import pprint
def locate_dust():
    is_dust = [[0] * R for _ in range(C)]
    for i in range(C):
        for j in range(R):
            if board[i][j] > 0:
                is_dust[i][j] = 1
    return is_dust

def flush():

    stash = []
    for c in range(C):
        for r in range(R):
            if is_dust[c][r]:
                extend = board[c][r]//5
                dir_cnt = 0

                for i in range(4):
                    nc = c + dc[i]; nr = r + dr[i]

                    if 0 <= nc < C and 0 <= nr < R and board[nc][nr] != -1:
                        stash.append((nc, nr, extend))
                        dir_cnt += 1
                
                board[c][r] = board[c][r] - board[c][r]//5 * dir_cnt
    
    for c, r, x in stash:
        board[c][r] += x

C, R, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(C)]

air_direction = [[[-1, 0], [0, 1], [1, 0], [0, -1]], [[1, 0], [0, 1], [-1, 0], [0, -1]]]
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
is_dust = locate_dust()
air_condi = []
for c in range(C):
    if board[c][0] == -1:
        air_condi.append((c, 0))

for _ in range(T):
    #미세먼지 확산
    flush()
    #공기청정기 가동
    for m in range(2):
        dir = air_direction[m]
        c, r = air_condi[m]
        for i in range(4):
            while True:
                nc = c + dir[i][0] 
                nr = r + dir[i][1]
                if 0 <= nc < C and 0 <= nr < R:
                    if board[nc][nr] == -1:
                        break

                    if m == 0:
                        if nc == air_condi[1][0]:
                            break
                    if m == 1:
                        if nc == air_condi[0][0]:
                            break

                    if board[c][r] != -1:
                        board[c][r] = board[nc][nr]
                        board[nc][nr] = 0
                    else:
                        board[nc][nr] = 0
                else:
                    break
                c = nc
                r = nr
    is_dust = locate_dust()

result = 0
for c in range(C):
    for r in range(R):
        result += board[c][r]
print(result + 2)




