import sys; read = sys.stdin.read
from collections import defaultdict, deque
tmp = list(map(int,read().split()))
tmp2 = [[tmp[x],tmp[x+1]] for x in range(0,len(tmp)-1,2)]
case_inp = []

sidx = 0

anw = []
for idx, x in enumerate(tmp2):
    if x == [0,0]:
        case_inp.append(tmp2[sidx:idx])
        sidx = idx+1
for inp in case_inp:

    adj = defaultdict(list)
    root = dict()

    # 1. root -> 들어오는 간선이 없는 노드는 단 한개
    # 2. 모든 노드에는 단 하나의 들어오는 간선
    # 3. 루트에서 다른 노드로 단일 경로로 갈 수 있어야함

    # 2
    if not inp:
        anw.append(True)
        continue

    anwb = True
    for x in inp:
        adj[x[0]].append(x[1])
        if root.get(x[1]) == None:
            root[x[1]] = x[0]
        else:
            anwb = False
            break
    if not anwb:
        anw.append(anwb)
        continue

    # 1
    root_cnt = 0
    for x in adj.keys():
        if x not in root.keys():
            root_cnt += 1
            root_node = x
    if root_cnt != 1:
        anw.append(False)
        continue

    # 3
    Q = deque([root_node])

    while Q:
        n = Q.popleft()
        for v in adj[n]:
            root[v] = False
            Q.append(v)

    if all(root.values()):
        anw.append(False)
        continue


    anw.append(True)


for idx, x in enumerate(anw):
    if x:
        print(f'Case {idx+1} is a tree.')
    else:
        print(f'Case {idx + 1} is not a tree.')