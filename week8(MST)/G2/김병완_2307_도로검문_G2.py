import sys; sys.stdin = open('2307_도로검문_G2.txt', 'r')
from heapq import heappush, heappop
input = sys.stdin.readline

def dijik(s, e):
    INF = float('inf')
    D = [INF] * (N + 1)
    visit = [False] * (N + 1)

    D[1] = 0
    Q = [(D[1], 1)]

    while Q:
        d, u = heappop(Q)
        if d > D[u]: continue
        visit[u] = True

        for v, w in nodes[u]:
            if u == s and v == e or u == e and v == s: continue
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q, (D[v], v))
                if s == 0:
                    p[v] = u
    return D[N]

N, M = map(int, input().split())
nodes = [[] for _ in range(N + 1)]

for idx in range(M):
    a, b, t = map(int, input().split())
    nodes[a].append((b, t))
    nodes[b].append((a, t))

p = [i for i in range(N + 1)]
noblock = dijik(0, 0)
result = 0

for block in range(N, 0, -1):
    tmp = dijik(p[block], block)
    if tmp == float('inf'):
        result = -1
        break
    result = max(tmp - noblock, result)

print(result)