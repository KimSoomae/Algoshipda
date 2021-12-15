# 백준 1167 골드 3 - 트리의 지름
from collections import defaultdict
# 각 노드까지의 거리 구하기
def dfs(idx, dis):
    global anw, visit, maxidx
    flag = False
    visit[idx] = 1
    for (node, new_dis) in d[idx]:
        if visit[node] == 0:
            flag = True
            dfs(node, dis + new_dis)
    if flag == False:
        if dis > anw:
            maxidx = idx
            anw = dis
    visit[idx] = 0

V = int(input())
d = defaultdict(list)
visit = [0] * (V + 1)
# maxidx는 임의의 점에서 최대 거리 가지는 노드의 번호
anw = 0; maxidx = -1
for _ in range(V):
    li = list(map(int, input().split()))
    for i in range(1, len(li), 2):
        if li[i] == -1: break
        d[li[0]].append((li[i], li[i + 1]))
# 임의의 노드에서 각 노드까지의 거리를 측정하여 최대 거리를 가지는 노드는 트리의 지름을 이루는 한 노드
# 일단 1번노드에서 dfs돌며 최대 거리 이루는 노드를 구하고
# 그 노드에서 시작하여 다시 dfs 돌면서 최대 거리 구하면 그게 트리의 지름
dfs(1, 0)
dfs(maxidx, 0)

print(anw)