import sys
sys.stdin = open('6416_트리인가_G5.txt', 'r')

input = sys.stdin.readline

ptoc = []
ctop = []
ptoc_tree = {}
ctop_tree = {}
uv = []
nod = set()
count = 0

def bfs(parent, field):
    if field.get(parent) is None:
        visit[parent] = 1
        return
    else:
        visit[parent] = 1
        for nod in field[parent]:
            bfs(nod, field)

while 1:
    read = list(map(int, input().split()))
    if read == []: continue
    for i in range(0, len(read), 2):
        if read[i] == 0 and read[i + 1] == 0:
            ptoc.append(ptoc_tree)
            ptoc_tree = {}
            ctop.append(ctop_tree)
            ctop_tree = {}
            uv.append((nod, count))
            nod = set()
            count = 0
            break
        if read[i] not in ptoc_tree:
            ptoc_tree[read[i]] = [read[i + 1]]
            nod.add(read[i])
            nod.add(read[i + 1])
            count += 1
        else:
            ptoc_tree[read[i]].append(read[i + 1])
            nod.add(read[i])
            nod.add(read[i + 1])
            count += 1
        if read[i + 1] not in ctop_tree:
            ctop_tree[read[i + 1]] = [read[i]]
        else:
            ctop_tree[read[i + 1]].append(read[i])
    N = len(read)
    if read[N - 2] < 0 and read[N - 1] < 0:
        break

for tc in range(len(ptoc)):
    result = 'a tree'
    # empty list is tree!
    if len(uv[tc][0]) == 0 and uv[tc][1] == 0:
        print(f'Case {tc + 1} is {result}.')
        continue
    # relationship between nod and line
    if uv[tc][1] != len(uv[tc][0]) - 1:
        result = 'not a tree'
        print(f'Case {tc + 1} is {result}.')
        continue
    # checking case 2
    for key in ctop[tc]:
        if key in ctop[tc][key]:
            result = 'not a tree'
            break
        if len(ctop[tc][key]) != 1:
            result = 'not a tree'
            break
    if result != 'a tree':
        print(f'Case {tc + 1} is {result}.')
        continue
    # checking case 1
    root_cnt = 0
    root = 0
    for key1 in ptoc[tc]:
        para = 0
        for key2 in ptoc[tc]:
            if key1 == key2: continue
            if key1 in ptoc[tc][key2]:
                para += 1
                break
        if para == 0:
            root = key1
            root_cnt += 1
        if root_cnt > 1:
            result = 'not a tree'
            break
    if root_cnt == 0:
        result = 'not a tree'
    if result != 'a tree':
        print(f'Case {tc + 1} is {result}.')
        continue
    # checking case 3
    # n = 0
    # for key in ptoc[tc]:
    #     if key == root: continue
    #     if key in ptoc[tc][root]:
    #         n += 1
    # if n != len(ptoc[tc]) - 1:
    #     result = 'not a tree'
    visit = [0] * (max(uv[tc][0]) + 1)
    bfs(root, ptoc[tc])
    for num in uv[tc][0]:
        if visit[num] == 0:
            result = 'not a tree'

    print(f'Case {tc + 1} is {result}.')




