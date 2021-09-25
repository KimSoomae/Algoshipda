import sys
sys.stdin = open('input.txt')

height = int(input())
board = []


if height > 1:
    for i in range(height):
        temp = list(map(int, input().split()))
        board.append(temp)

    dp = []
    dp.append(board[0])
    dp.append([board[0][0]+board[1][0], board[0][0] + board[1][1]])

    for i in range(2, height):
        temp = []
        for j in range(i):
            if j == 0:
                temp.append(dp[-1][j] + board[i][j])
                temp.append(dp[-1][j] + board[i][j+1])
            else:
                if temp[-1] < dp[-1][j] + board[i][j]:
                    temp.pop()
                    temp.append(dp[-1][j] + board[i][j])
                else:
                    pass
                temp.append(dp[-1][j] + board[i][j+1])

        dp.append(temp)

    print(max(dp[-1]))
else:
    print(int(input()))