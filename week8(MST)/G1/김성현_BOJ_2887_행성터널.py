input = open('input.txt').readline

def Find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union(x, y):
    root_x, root_y = Find_set(x), Find_set(y)
    p[max(root_x, root_y)] = min(root_x, root_y)

N = int(input())
p = [i for i in range(N+1)]

board = []
for i in range(1, N+1):
    x, y, z = map(int, input().split())
    board.append((x, y, z, i))

G = []
for i in range(3):
    board.sort(key=lambda x : x[i])
    
    for j in range(N-1):
        G.append((abs(board[j][i]- board[j+1][i]), board[j][3], board[j+1][3]))        

G.sort(key=lambda x : x[0])


count = 0
Total_cost = 0
for val, i, j in G:
    if Find_set(i) != Find_set(j):
        Total_cost += val
        Union(i, j)
        count += 1
        
    if count == N-1:
        break
print(Total_cost)
