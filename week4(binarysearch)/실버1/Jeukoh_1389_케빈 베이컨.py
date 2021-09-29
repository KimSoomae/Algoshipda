import sys; readline = sys.stdin.readline
N, M = map(int,readline().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int,readline().split())
    adj[i][j] = 1
    adj[j][i] = 1

for k in range(1,N+1):
    for x in range(1,N+1):
        for y in range(1,N+1):
            if x == k or y == k or x == y:
                continue
            if adj[x][k] and adj[k][y]:
                if adj[x][y]:
                    adj[x][y] = min(adj[x][y], adj[x][k]+adj[k][y])
                else:
                    adj[x][y] = adj[x][k]+adj[k][y]

anw_list = []
min_v = 1000000
min_idx = 0
for idx in range(N,0,-1):
    v = adj[idx]
    tmp = sum(v)
    if tmp <= min_v:
        min_v = tmp
        min_idx = idx

#print(adj)
print(min_idx)