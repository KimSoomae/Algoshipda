import sys;

readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict

N = int(input())
value = [0] * (N + 1)
adj = defaultdict(list)
for idx in range(2, N + 1):
    l = readline().split()
    if l[0] == 'S':
        value[idx] = int(l[1])
    else:
        value[idx] = -int(l[1])
    adj[int(l[2])].append(idx)


def dfs(node):
    if adj.get(node):
        for v in adj[node]:
            value[node] += dfs(v)

    if value[node] < 0:
        return 0
    else:
        return value[node]


dfs(1)
print(value[1])

''':var
다른 풀이

import sys
input = sys.stdin.readline

n = int(input())
parent = [0]*(n+1)
cost = [0]*(n+1)
ind = [0]*(n+1)
for i in range(2,n+1):
    s = input().split()
    cost[i],parent[i] = map(int, s[1:])
    ind[parent[i]] += 1
    if s[0] == 'W': cost[i] = -cost[i]

q = [i for i in range(2,n+1) if ind[i] == 0]
while q:
    cur = q.pop()
    if cost[cur] < 0:
        cost[cur] = 0
    next = parent[cur]

    cost[next] += cost[cur]
    ind[next] -= 1
    if ind[next] == 0:
        q += [next]
print(cost[1])


'''