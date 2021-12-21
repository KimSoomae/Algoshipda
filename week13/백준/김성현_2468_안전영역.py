input = open('input.txt').readline
N = int(input())

board = []
max_height = 0
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def dfs(height):
    land_number = 0

    visited = [[0] * N for _ in range(N)]
    q = []

    for c in range(N):
        for r in range(N):
            if board[c][r] <= height:
                visited[c][r] = 1
    
    for c in range(N):
        for r in range(N):
            if not visited[c][r]:
                visited[c][r] = 1
                land_number += 1
                q.append((c, r))

                while q:
                    c, r = q.pop()
                    for i in range(4):
                        nc = c + dc[i]; nr = r + dr[i]

                        if 0 <= nc < N and 0 <= nr < N:
                            if not visited[nc][nr]:
                                visited[nc][nr] = 1
                                q.append((nc, nr))
    return land_number    

for _ in range(N):
    line = list(map(int, input().split()))
    max_height = max(max_height, max(line))
    board.append(line)

answer = 0
for i in range(max_height + 1):
    answer = max(answer, dfs(i))
print(answer)


