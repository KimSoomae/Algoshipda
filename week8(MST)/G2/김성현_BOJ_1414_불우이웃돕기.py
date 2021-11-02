#MST

input = open('input.txt').readline
N = int(input().strip())

def converter(ch):
    if ch == ch.upper():
        return ord(ch)-38
    else:
        return ord(ch)-96

def Find_set(x):
    while x != p[x]: x = p[x]
    return x

def Union(x, y):
    root_x, root_y = Find_set(x), Find_set(y)
    p[max(root_x, root_y)] = min(root_x, root_y)


board = [[0] * (N+1)]
for i in range(1, N+1):
    i_lans = [0] + list(input().strip())
    board.append(i_lans)

G = []
donation = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if board[i][j] != '0' and i != j:
            u, v, val = i, j, converter(board[i][j])
            donation += val
            G.append((u, v, val))

        if board[i][j] != '0' and i == j:
            donation += converter(board[i][j])

G.sort(key=lambda x : x[2])

p = [i for i in range(N+1)]
cnt = 0

for u, v, val in G:

    if Find_set(u) != Find_set(v):
        Union(u, v)
        cnt += 1
        donation -= val

        if cnt == N-1:
            break
if cnt != N-1:
    donation = -1

print(donation)

