# 백준 1068 트리 - 트리 골드5 김수민
from collections import deque
N = int(input())
arr = list(map(int, input().split()))
erase = int(input())
P = [-2] * (N + 1) # 부모 저장
child = [[] for _ in range(N + 1)] # 자식 저장
Q = deque()
# 각 노드의 부모 저장
for node in enumerate(arr):
    idx, par = node
    P[idx] = par
# 각 노드의 자식 저장
for i in range(N):
    if P[i] == -1:
        root = i
    else:
        child[P[i]].append(i)
anw = 0
# 루트가 지울게 아니라면 Q에 추가
if root != erase:
    Q.append(root)
# 자식 추가해주며 bfs 돌기
while Q:
    parent = Q.popleft()
    flag = False
    # 자식 Q에 추가해주는데 한번이라도 걸리면 리프노드 아닌거니까 flag True로 업데이트
    for children in child[parent]:
        if children == erase: continue
        Q.append(children)
        flag = True
    # for문 안걸렸으면 자식 노드 하나도 없는 거니까 리프노드 해당
    if flag == False:
        anw += 1
print(anw)