input = open('input.txt').readline


dc = [0, -1, 0, 1]
dr = [1, 0, -1, 0]

n = int(input())

board = [[0] * 101 for _ in range(101)]

for i in range(n):

    r, c, d, g = map(int, input().split())
    board[c][r] = 1
    
    temp = [d]
    q = [d]

    for _ in range(g+1):
        for k in q:
            c += dc[k]
            r += dr[k]
            board[c][r] = 1
        
        q = [(i+1) % 4 for i in temp]
        q.reverse()
        temp = temp + q
result = 0

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

print(result)

