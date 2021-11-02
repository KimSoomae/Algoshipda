import sys; sys.stdin = open('1277_발전소설치.txt', 'r')
from heapq import heappush, heappop
input = sys.stdin.readline

N, W = map(int, input().split())
M = float(input())
rows = []
cols = []
for _ in range(N):
    row, col = map(int, input().split())
    rows.append(row)
    cols.append(col)

# min_r = min(rows)
# max_r = max(rows)
# min_c = min(cols)
# max_c = max(cols)
# r_len = max_r - min_r + 1
# c_len = max_c - min_c + 1
# field = [[0] * c_len for _ in range(r_len)]
# for i in range(N):
#     field[rows[i] + abs(min_r)][cols[i] + abs(min_c)] = (i + 1)

link = [[] for _ in range(N)]
for _ in range(W):
    node1, node2 = map(int, input().split())
    link[node1 - 1].append(node2 - 1)
    link[node2 - 1].append(node1 - 1)

INF = float('inf')
D = [INF] * N
p = [i for i in range(N)]
visit = [False] * N
D[0] = 0
Q = [(D[0], 0)]

while Q:
    d, u = heappop(Q)
    if d > D[u]: continue
    visit[u] = True
    for v in range(N):
        if v == u: continue
        w = ((rows[v] - rows[u]) ** 2 + (cols[v] - cols[u]) ** 2) ** 0.5
        if abs(w - M) < 10 ** (-3): continue
        if v in link[u]: w = 0
        if not visit[v] and D[v] > D[u] + w:
            D[v] = D[u] + w
            p[v] = u
            heappush(Q, (D[v], v))


print(int(D[N-1] * 1000))