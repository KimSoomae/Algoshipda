input = open('input.txt').readline
from pprint import pprint
C, R = map(int, input().split())

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
del_cordintate = []
def delete_land(c, r):
    cnt = 0
    for i in range(4):
        nc = c + dc[i]; nr = r + dr[i]
        if 0 <= nc < C and 0 <= nr < R:
            if board[nc][nr] == '.':
                cnt += 1
        else:
            cnt += 1
    if cnt >= 3:
        del_cordintate.append((c, r))

board = [list(input().strip()) for _ in range(C)]
for c in range(C):
    for r in range(R):
        if board[c][r] == 'X':
            delete_land(c, r)

for cor in del_cordintate:
    c, r = cor
    board[c][r] = '.'

upper, lower, left, right = False, False, False, False
for c in range(C):
    for r in range(R):
        if board[c][r] == 'X':
            upper_bound = c
            upper = True
            break
    if upper:
        break


for c in range(C-1, -1, -1):
    for r in range(R):
        if board[c][r] == 'X':
            lower_bound = c
            lower = True
            break
    if lower:
        break

for r in range(R):
    for c in range(C):
        if board[c][r] == 'X':
            left_bound = r
            left = True
            break
    if left:
        break

for r in range(R-1, -1, -1):
    for c in range(C):
        if board[c][r] == 'X':
            right_bound = r
            right = True
    if right:
        break

for c in range(upper_bound, lower_bound+1):
    for r in range(left_bound, right_bound+1):
        print(board[c][r], end='')
    print()