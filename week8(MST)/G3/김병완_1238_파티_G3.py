import sys; sys.stdin = open('1238_파티_G3.txt', 'r')
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start, end):
    INF = float('inf')
    D = [INF] * (N + 1)
    visit = [False] * (N + 1)
    p = [i for i in range(N + 1)]
    D[start] = 0
    Q = [(D[start], start)]

    while Q:
        d, u = heappop(Q)
        if d > D[u]: continue
        visit[u] = True
        if u == end: break

        for v, w in link[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                p[v] = u
                heappush(Q, (D[v], v))
    return D[end]

N, M, X = map(int, input().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    link[s].append((e, t))
ans = [0] * (N + 1)
for person in range(1, N + 1):
    # INF = float('inf')
    # D = [INF] * (N + 1)
    # visit = [False] * (N + 1)
    # p = [i for i in range(N + 1)]
    # D[person] = 0
    # Q = [(D[person], person)]
    #
    # while Q:
    #     d, u = heappop(Q)
    #     if d > D[u]: continue
    #     visit[u] = True
    #     if u == X: break
    #
    #     for v, w in link[u]:
    #         if not visit[v] and D[v] > D[u] + w:
    #             D[v] = D[u] + w
    #             p[v] = u
    #             heappush(Q, (D[v], v))

    ans[person] = dijkstra(person, X) + dijkstra(X, person)

print(max(ans))