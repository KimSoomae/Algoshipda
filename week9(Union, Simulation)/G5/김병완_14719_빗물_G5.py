import sys; sys.stdin = open('14719_빗물_G5.txt', 'r')

input = sys.stdin.readline
H, W = map(int, input().split())
info = list(map(int, input().split()))
board = [[0] * W for _ in range(H)]
for i in range(W):
    for j in range(info[i]):
        board[H - 1 - j][i] = 1
cnt = 0
for row in range(H):
    start = -1
    end = -1
    for col in range(W):
        if board[row][col]:
            start = end
            end = col
            if start != -1:
                cnt += col - start - 1

print(cnt)