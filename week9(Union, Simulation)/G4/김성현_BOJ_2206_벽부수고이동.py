input = open('input.txt').readline

C, R = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(C)]

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
visited = [[0]*R for _ in range(C)]

def bfs():
    cnt = 0
    Q = []
    Q.append((0, 0, 0))
    visited[0][0] = 1
    while Q:
        temp = []
        while Q:
            c, r, w = Q.pop()
            if (c, r) == (C-1, R-1):
                return cnt+1
            visited[c][r] = 1
            for i in range(4):
                new_c = c + dc[i]
                new_r = r + dr[i]

                if 0 <= new_c <= C-1 and 0 <= new_r <= R-1:
                    if board[new_c][new_r] == 0 and not visited[new_c][new_r]:
                        temp.append((new_c, new_r, w))

                    elif board[new_c][new_r] == 1 and w == 0 and not visited[new_c][new_r]:
                        temp.append((new_c, new_r, 1))
        
        for x in temp:
            Q.append(x)
        cnt += 1
    
    return -1


result = bfs()
print(result)