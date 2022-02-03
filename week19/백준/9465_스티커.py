input = open('input.txt').readline
TC = int(input())

for _ in range(TC):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]

    for j in range(1, n):
        if j == 1:
            board[0][j] += board[1][j-1]
            board[1][j] += board[0][j-1]
        else:
            board[0][j] += max(board[1][j-1], board[1][j-2])
            board[1][j] += max(board[0][j-1], board[0][j-2])
    print(max(board[0][n-1], board[1][n-1]))