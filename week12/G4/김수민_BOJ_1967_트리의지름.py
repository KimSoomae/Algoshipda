# BOJ 1967 골드4 - 트리의지름
from collections import defaultdict
import sys
# Recursion Error 방지- 재귀의 한도 100000까지 풀어주기
sys.setrecursionlimit(100000)
# 임의의 지점에서 최대 거리 구하기
def dfs(node, distance):
    global anw, maxidx
    visit[node] = 1
    flag = False
    for (e, w) in dis[node]:
        if visit[e]: continue
        flag = True
        dfs(e, distance + w)
    if flag == False:
        if distance > anw:
            maxidx = node
            anw = distance
    visit[node] = 0


N = int(input())
dis = defaultdict(list)
anw = 0; maxidx = 0
visit = [0] * (N + 1)
for _ in range(N - 1):
    v, e, w = map(int, input().split())
    dis[v].append((e, w))
    dis[e].append((v, w))

# 루트노드에서 제일 거리의 합이 큰 지점을 찾아
dfs(1, 0)
# 그 지점에서 dfs 돌며 트리의 지름 찾기
dfs(maxidx, 0)
print(anw)