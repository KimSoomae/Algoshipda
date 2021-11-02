import sys; sys.stdin = open('13418_학교탐방하기_G3.txt', 'r')
input = sys.stdin.readline

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(nod):
    result = 0
    cnt = 0
    for w, u, v in nod:
        if find_set(u) != find_set(v):
            cnt += 1
            result += w
            p[find_set(v)] = find_set(u)
            if cnt == V:
                break
    return result

V, E = map(int, input().split())
min_nod = []
max_nod = []
for _ in range(E + 1):
    s, e, w = map(int, input().split())
    w = (w + 1) % 2
    min_nod.append((w, s, e))
    max_nod.append((w, s, e))

min_nod.sort()
max_nod.sort(reverse=True)
p = [i for i in range(V + 1)]
a = union(max_nod) ** 2
p = [i for i in range(V + 1)]
b = union(min_nod) ** 2

print(a-b)
