import sys; sys.stdin = open('17149_이차원배열과연산_G4.txt', 'r')
from collections import defaultdict
input = sys.stdin.readline

def r_cal(row, col, arr):
    max_len = 0
    board = []
    for i in range(row):
        tmp = defaultdict(int)
        for j in range(col):
            if not arr[i][j]: continue
            tmp[arr[i][j]] += 1

        tmp = {k: v for k, v in sorted(tmp.items(), key=lambda x: (x[1], x[0]))}
        new = []
        for key in tmp:
            new.append(key)
            new.append(tmp[key])
        if len(new) > max_len:
            max_len = len(new)
        board.append(new)
    if max_len < 3:
        max_len = 3
    for lis in board:
        if len(lis) < max_len:
            diff = max_len - len(lis)
            lis += [0] * diff
    return (row, max_len, board)


def c_cal(row, col, arr):
    tmp = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            tmp[j][i] = arr[i][j]

    c, r, board = r_cal(col, row, tmp)
    tmp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            tmp[i][j] = board[j][i]
    return (r, c, tmp)


def isAnswer():
    # Runtime Error의 원인
    if r > r_len or c > c_len: return False
    if board[r - 1][c - 1] == k:
        return True
    return False

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

r_len = 3
c_len = 3
flag = True
result = -1
if isAnswer():
    result = 0
    flag = False

cnt = 0
while flag:
    cnt += 1
    if r_len >= c_len:
        r_len, c_len, board = r_cal(r_len, c_len, board)
        if isAnswer():
            result = cnt
            flag = False
    else:
        r_len, c_len, board = c_cal(r_len, c_len, board)
        if isAnswer():
            result = cnt
            flag = False

    if cnt > 100:
        break

print(result)
