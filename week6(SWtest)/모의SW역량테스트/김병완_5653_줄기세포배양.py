# import sys; sys.stdin = open('5653_줄기세포배양.txt', 'r')
# division 분해해서 timeticking에 집어 넣을것
def initialize(r, c, board):
    # (value, status, time)
    tmp_board = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                tmp_board[i][j] = (board[i][j], 1, 0)
            else:
                tmp_board[i][j] = (0, 0, 0)
    return tmp_board

# def timeticking(r, c, board):
#     # dead : 3 / act : 2 / pre-act : 1
#     tmp_board = [[] for _ in range(r)]
#     for i in range(r):
#         tmp_board[i] = board[i][:]
#         for j in range(c):
#             if tmp_board[i][j]:
#                 if tmp_board[i][j][1] == 3:continue
#                 if tmp_board[i][j][0] == tmp_board[i][j][2] + 1:
#                     tmp_board[i][j] = (tmp_board[i][j][0], tmp_board[i][j][1] + 1, 0)
#                 else:
#                     tmp_board[i][j] = (tmp_board[i][j][0], tmp_board[i][j][1], tmp_board[i][j][2] + 1)
#     return tmp_board

# modifying...

# 시간이 흐르고 분열하는 기능
def timeticking(r, c, board):
    # 시간이 흐르는 부분 구현
    # dead : 3 / act : 2 / pre-act : 1
    tmp_board = [[] for _ in range(r)]
    for i in range(r):
        tmp_board[i] = board[i][:]
    tmp = []
    for i in range(r):
        for j in range(c):
            if tmp_board[i][j][1] == 3:
                continue
            elif tmp_board[i][j][1] == 2:
                tmp.append((i, j))
                if tmp_board[i][j][0] == tmp_board[i][j][2] + 1:
                    tmp_board[i][j] = (tmp_board[i][j][0], 3, 0)
                else:
                    tmp_board[i][j] = (tmp_board[i][j][0], tmp_board[i][j][1], tmp_board[i][j][2] + 1)
            elif tmp_board[i][j][1] == 1:
                if tmp_board[i][j][0] == tmp_board[i][j][2] + 1:
                    tmp_board[i][j] = (tmp_board[i][j][0], tmp_board[i][j][1] + 1, 0)
                else:
                    tmp_board[i][j] = (tmp_board[i][j][0], tmp_board[i][j][1], tmp_board[i][j][2] + 1)
    # 분열할 곳들 분열시키기
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for r, c in tmp:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if board[nr][nc] != (0, 0, 0): continue
            # 분열이 겹치는 부분에서 애먹음 DEBUG찾는거 고생
            if tmp_board[nr][nc] != (0, 0, 0) and tmp_board[nr][nc][0] < tmp_board[r][c][0]:
                tmp_board[nr][nc] = (tmp_board[r][c][0], 1, 0)
            elif tmp_board[nr][nc] == (0, 0, 0):
                tmp_board[nr][nc] = (tmp_board[r][c][0], 1, 0)
    return tmp_board

# 무한한 배양틀에서 배양틀을 지속적으로 확인하고 늘리는 함수
def enlarge(r, c, board):
    tmp = [[] for _ in range(r)]
    # 첫번째 행과 마지막 행만 확인하는 작업
    for i in range(r):
        tmp[i] = board[i][:]
    nr = r; nc = c
    for i in range(nr):
        if tmp[i][0][1] == 2:
            for k in range(r):
                tmp[k] = [(0, 0, 0)] + tmp[k]
            nc += 1
            break
    for i in range(nr):
        if tmp[i][nc - 1][1] == 2:
            for k in range(r):
                tmp[k].append((0, 0, 0))
            nc += 1
            break
    # 첫번째 열과 마지막 열만 확인
    for j in range(nc):
        if tmp[0][j][1] == 2:
            tmp.insert(0, [(0, 0, 0)] * nc)
            nr += 1
            break

    for j in range(nc):
        if tmp[nr - 1][j][1] == 2:
            tmp.append([(0, 0, 0)] * nc)
            nr += 1
            break
    return (nr, nc, tmp)


# def division(r, c, board):
#     tmp = [[] for _ in range(r)]
#     for idx in range(r):
#         tmp[idx] = board[idx][:]
#
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     for i in range(r):
#         for j in range(c):
#             if tmp[i][j]:
#                 if tmp[i][j][1] == 2:
#                     for k in range(4):
#                         nr = i + dr[k]
#                         nc = j + dc[k]
#                         if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
#                         if tmp[nr][nc]: continue
#                         tmp[nr][nc] = (tmp[i][j][0], 1, 0)
#
#     return tmp

# 마지막 활성화, 비활성화 세포 숫자 세기
def cal_lives(r, c, board):
    cnt = 0
    for i in range(r):
        for j in range(c):
            if board[i][j][1] == 1 or board[i][j][1] == 2:
                cnt += 1
    return cnt

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(N)]
    board = initialize(N, M, cells)
    # board = timeticking(N, M, board)
    # N, M, board = enlarge(N, M, board)
    for _ in range(K):
        # board = division(N, M, board)
        N, M, board = enlarge(N, M, board)
        board = timeticking(N, M, board)

    result = cal_lives(N, M, board)
    print('#{} {}'.format(tc, result))


