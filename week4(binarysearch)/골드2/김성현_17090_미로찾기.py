import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(input()))

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}
# board, visited : (True, 1), ('RLUD', 1), ('RLUD', 0)
visited = [[0] * M for _ in range(N)]

def go(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return True

    if board[i][j] == True:
        return True
    
    if visited[i][j]:
        return False

    else:
        visited[i][j] = 1

        di, dj = directions[board[i][j]]
        new_i = i + di; new_j = j + dj

        res = go(new_i, new_j)
        if res:
            board[i][j] = True
        return res
    


cnt = 0
for i in range(N):
    for j in range(M):
        if go(i, j):
            cnt += 1

print(cnt)

#실패작 1#
'''
def go(i, j):
    if (i, j) in visited:
        for tup in visited:
            cannnot_exit.append(tup)
        return False
    
    elif board[i][j] == 0:
        for tup in visited:
            can_exit.append(tup)
        return True

    visited.append((i, j))

    di, dj = directions[board[i][j]]
    i += di; j += dj
    return go(i, j)
'''


#실패작 2#
'''
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

board = [[0] * (M+2)]

for _ in range(N):
    board.append([0] + list(input()) + [0])

board.append([0] * (M+2))

can_exit = []
cannnot_exit = []

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
    'X': (0, 0)
}
def go(i, j):
    if (i, j) in visited:
        for (i, j) in visited:
            board[i][j] = 'X'
        return False
    else:
        visited.append((i, j))
        di, dj = directions[board[i][j]]
        i += di ; j += dj
        
        if board[i][j] == 'X':
            return False
        else:
            if board[i][j] == 0:
                return True
            else:
                return go(i, j)

cnt = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 'X':
            pass
        else:
            visited = []
            if go(i, j):
                cnt += 1
    
print(cnt)


'''