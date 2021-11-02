import sys; sys.stdin = open('1197_최소스패닝트리_G4.txt', 'r')
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
nodes = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    nodes[A].append((C, B))
    nodes[B].append((C, A))

INF = float('inf')
key = [INF] * (V + 1)
pi = [0] * (V + 1)
group = [0] * (V + 1)
key[1] = 0
Q = [(key[1], 1)]
cnt = 0
result = 0
while Q:
    if cnt == V:
        break

    p, u = heappop(Q)

    if group[u]: continue
    group[u] = 1
    result += p
    cnt += 1
    for w, v in nodes[u]:
        key[v] = w
        heappush(Q, (key[v], v))
        pi[v] = u

print(result)