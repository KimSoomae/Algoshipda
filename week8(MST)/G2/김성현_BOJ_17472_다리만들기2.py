input = open('input.txt').readline
from pprint import pprint
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def dfs(c, r, cnt): #각 구역을 넘버링하는 함수
    board[c][r] = cnt
    visited[c][r] = 1

    temp.append((c, r))
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]

        if 0 <= nc <= C-1 and 0 <= nr <= R-1:
            if board[nc][nr] and not visited[nc][nr]:
                dfs(nc, nr, cnt)
    

def find_bridge(c, r, number):
    start_bridge = board[c][r]
    initial_c = c
    initial_r = r
    for i in range(4):
        c = initial_c
        r = initial_r

        length = 0
        while 0 <= c+dc[i] <= C-1 and 0 <= r+dr[i] <= R-1:
            c += dc[i]; r += dr[i]
            if board[c][r] == 0:
                length += 1
            else:
                break
        if board[c][r] != number and board[c][r] != 0:
            end_bridge = board[c][r]
            if length != 1 and (start_bridge, end_bridge, length) not in MST_graph and (end_bridge, start_bridge, length) not in MST_graph:
                MST_graph.append((start_bridge, end_bridge, length))
        
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union(x, y):
    root_x, root_y = find_set(x), find_set(y)
    p[max(root_x, root_y)] = min(root_x, root_y)


C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(C)]
visited = [[0]*R for _ in range(C)]

G = []
cnt = 0
for c in range(C):
    for r in range(R):
        if board[c][r] and not visited[c][r]:
            cnt += 1
            temp = []
            dfs(c, r, cnt)
            G += [temp]

MST_graph = []

for i in range(cnt - 1):
    G_list = G.pop()

    for c, r in G_list:
        find_bridge(c, r, board[c][r])


# KRUSKAL
if MST_graph:
    MST_graph.sort(key=lambda x: x[2])
    p = [i for i in range(cnt+1)]
    bridge_cnt = 0
    bridge_length = 0
    made = True
    for u, v, val in MST_graph:
        
        if find_set(u) != find_set(v):
            Union(u, v)
            bridge_length += val
            bridge_cnt += 1
        if bridge_cnt == cnt-1:
            break
    if bridge_cnt != cnt-1:
        print(-1)
    else:
        print(bridge_length)
    
else:
    print(-1)

