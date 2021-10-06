# 11725 트리의 부모 찾기 - 트리 S2 김수민
from collections import deque
N = int(input())
P = [0] * (N + 1) # 부모 저장
find = [0] * (N + 1) # 부모 찾았는지 확인
link = [[] for _ in range(N + 1)]
Q = deque() # 자식찾을 부모들 후보
for i in range(N - 1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
find[1] = 1
Q.append(1)
while Q:
    parent = Q.popleft()
    children = link[parent] # 부모에 연결된 자식들
    for child in children:
        if not find[child]: # 부모 안찾았은 자식이면
            P[child] = parent # 부모 연결
            find[child] = 1
            Q.append(child)

for i in range(2, N + 1):
    print(P[i])