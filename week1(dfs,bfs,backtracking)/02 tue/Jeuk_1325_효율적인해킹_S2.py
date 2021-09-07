import sys; readline = sys.stdin.readline
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
N, M = map(int,readline().split())

# 3. dfs

# adj = defaultdict(list)
# for _ in range(M):
#     a, b = map(int,readline().split())
#     adj[a].append(b)
#
# visited = [-1]+[1]*N
# def dfs(i,x):
#     for v in adj[x]:
#         if visited[v] < i+1:
#             visited[v] = i+1
#             dfs(i+1,v)
#
# for x in range(1,N+1):
#     if visited[x] == 1:
#         dfs(1,x)
#
# max_v = 0
# stack = []
# for idx,v in enumerate(visited):
#     if v > max_v:
#         stack = [idx]
#         max_v = v
#     elif v == max_v:
#         stack.append(idx)
#
# print(' '.join(str(x) for x in stack))

# 2. bfs

adj = defaultdict(list)
for _ in range(M):
    a, b = map(int,readline().split())
    adj[b].append(a)

vistied = [False]+[True]*N

def bfs(x):
    cnt = 1
    visited = [False] + [True] * N
    Q = deque([x])
    visited[x] = False
    while Q:
        nx = Q.popleft()
        cnt += 1
        for v in adj[nx]:
            if visited[v]:
                visited[v] = False
                Q.append(v)

    return cnt

max_v = 0
stack = []
for idx in range(1,N+1):
    v = bfs(idx)

    if v > max_v:
        stack = [idx]
        max_v = v
    elif v == max_v:
        stack.append(idx)



print(' '.join(str(x) for x in stack))



# 1. recursive

# visited = [0]*(N+1)
#
# def recursive(x):
#     if visited[x]:
#         return visited[x]
#     else:
#         ret = 1
#         for v in adj[x]:
#             ret += recursive(v)
#         visited[x] = ret
#         return ret
#
# for _ in range(1,N+1):
#     if not visited[_]:
#         recursive(_)
# max_v = 0
# stack = []
# for idx,v in enumerate(visited):
#     if v > max_v:
#         stack = [idx]
#         max_v = v
#     elif v == max_v:
#         stack.append(idx)