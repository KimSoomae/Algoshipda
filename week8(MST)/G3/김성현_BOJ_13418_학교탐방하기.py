input = open('input.txt').readline

def find_set(x):
    while x != p[x]: x = p[x]
    return x

def Union(a, b):
    root_a, root_b = find_set(a), find_set(b)
    p[max(root_a, root_b)] = min(root_a, root_b)

N, M = map(int, input().split())

G = [tuple(map(int, input().split()))]
reversed_G = G[:]

no_G = []
reversed_no_G = []
for _ in range(M):
    u, v, d = map(int, input().split())

    if d:
        G.append((u, v, d))
        reversed_no_G.append((u, v, d))
    else:
        no_G.append((u, v, d))
        reversed_G.append((u, v, d))

G += no_G
reversed_G += reversed_no_G

tired = 0
clean = 0
cnt = 0
p = [i for i in range(N+1)]
for u, v, d in G:

    if find_set(u) != find_set(v):
        Union(u, v)
        
        if not d:
            clean += 1
        
        cnt += 1

    if cnt == N:
        break

p = [i for i in range(N+1)]
for u, v, d in reversed_G:
    if find_set(u) != find_set(v):
        Union(u, v)
        
        if not d:
            tired += 1
        
        cnt += 1

    if cnt == N:
        break

print(tired**2 - clean**2)
