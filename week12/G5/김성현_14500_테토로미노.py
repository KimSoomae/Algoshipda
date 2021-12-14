from pprint import pprint
input = open('input.txt').readline

C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(C)]


dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]


def tetro(c, r, n, total):
    global max_val

    if max_val >= total + dev * (4-n):
        return

    if n == 4:
        max_val = max(max_val, total)
        return 

    visited[c][r] = 1

    for i in range(4):
        new_c = c + dc[i]
        new_r = r + dr[i]

        if 0 <= new_c < C and 0 <= new_r < R:
            if not visited[new_c][new_r]:

                if n == 2:
                    
                    visited[new_c][new_r] = 1
                    tetro(c, r, n+1, total + board[new_c][new_r])
                    visited[new_c][new_r] = 0
                    

                
                visited[new_c][new_r] = 1
                tetro(new_c, new_r, n+1, total + board[new_c][new_r])
                
                visited[new_c][new_r] = 0

    pass

visited = [[0] * R for _ in range(C)]
max_val = 0
dev = max(map(max, board))
for c in range(C):
    for r in range(R):
        visited[c][r] = 1 
        tetro(c, r, 1, board[c][r])
        visited[c][r] = 0
print(max_val)
        

        
