import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

def bfs(i):
    global kevin
    visited[i] = 1
    Q = []

    for j in range(1, N+1):
        if board[i][j] == 1:
            visited[j] = 1
            Q.append(j)
    kevin = [[0], Q[:]] # kevin ; i번째 index에는 i번째 다리에 존재하는 사람들의 리스트 

    while Q:
        temp = []
        for _ in range(len(Q)):
            i = Q.pop()

            for j in range(1, N+1):
                if board[i][j] == 1 and not visited[j]:
                    temp.append(j)
                    visited[j] = 1

        for val in temp:
            Q.append(val)
        if temp:
            kevin.append(temp)


board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    board[i][j] = 1
    board[j][i] = 1

value_list = []
for i in range(1, N+1):

    visited = [0] * (N+1)
    bfs(i)

    value = 0
    for j in range(1, len(kevin)):
        value += len(kevin[j]) * j
    value_list.append(value)

min_val = min(value_list)
for i in range(N):
    if value_list[i] == min_val:
        print(i+1)
        break

