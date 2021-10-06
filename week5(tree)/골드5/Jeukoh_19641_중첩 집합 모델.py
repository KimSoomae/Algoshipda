import sys; read = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6)
def dfs(x,cnt):
    visited[x] = True
    anw[x][0] = cnt
    cnt += 1
    for v in adj[x]:
        if not visited[v]:
            cnt = dfs(v,cnt)

    anw[x][1] = cnt
    cnt += 1
    return cnt

NumNode = int(input())
adj = defaultdict(list)
for _ in range(NumNode):
    tmp = list(map(int,read().split()))
    adj[tmp[0]] = tmp[1:-1]
    adj[tmp[0]].sort()

root = int(input())
anw = [[0,0] for _ in range(NumNode+1)]
visited = [False]*(NumNode+1)
dfs(root,1)
for idx, v in enumerate(anw):
    if idx:
        print(' '.join(str(x) for x in [idx]+v))