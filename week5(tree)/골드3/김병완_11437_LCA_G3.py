import sys
sys.stdin = open('김병완_11437_LCA_G3.txt', 'r')
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def depth(n, dep):
    level[n] = dep
    visit[n] = 1
    for nod in info[n]:
        if visit[nod]: continue
        par0[nod] = n
        depth(nod, dep + 1)

def lca(a, b):
    if level[a] > level[b]:
        a, b = b, a
    for i in range(idx - 1, -1, -1):
        if level[par[i][b]] >= level[a]:
            b = par[i][b]

    if a == b:
        return a
    for i in range(idx - 1, -1, -1):
        if par[i][a] and par[i][b] and par[i][a] != par[i][b]:
            a = par[i][a]
            b = par[i][b]
    return par[0][a]


N = int(input())
info = [[] for _ in range(N + 1)]
level = [0] * (N + 1)
par0 = [0] * (N + 1)
for _ in range(N - 1):
    P, C = map(int, input().split())
    info[P].append(C)
    info[C].append(P)
visit = [0] * (N + 1)
depth(1, 1)
par = [par0]
deepest = max(level)
idx = 0
while deepest >= 1:
    deepest //= 2
    tmp1 = par[idx]
    tmp2 = [0] * (N + 1)
    for i in range(N + 1):
        tmp2[i] = tmp1[tmp1[i]]
    par.append(tmp2)
    idx += 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))
