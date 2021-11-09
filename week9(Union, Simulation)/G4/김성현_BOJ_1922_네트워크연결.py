input = open('input.txt').readline
from collections import deque

def KRUSKAL(G):
    mst = []

    mst_cost = 0
    for i in range(N):
        Make_set(i)

    while len(mst) < N-1:
        u, v, cost  = G.popleft()

        if Find_set(u) != Find_set(v):
            Union(u, v)
            mst_cost += cost
            mst.append((u, v))
    return mst_cost

def Make_set(x):
    p[x] = x
    rank[x] = 0

def Find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


N = int(input())

E = int(input())
G = []
for i in range(E):
    G.append(tuple(map(int, input().split())))
G.sort(key=lambda x : x[2])
G = deque(G)
p = [0] * (N+1)
rank = [0] * (N+1)

print(KRUSKAL(G))