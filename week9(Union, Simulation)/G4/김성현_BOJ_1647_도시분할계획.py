input = open('input.txt').readline

N, M = map(int, input().split())

G = []
for _ in range(M):
    u, v, val = map(int, input().split())
    G.append((u, v, val))

G.sort(key=lambda x: x[2])
cnt = 0
cost = 0

def find_set(x):
    while x != p[x]: x = p[x]
    return x

def Union(x, y):
    x = find_set(x)
    y = find_set(y)
    p[max(x, y)] = min(x, y)

p = [i for i in range(N+1)]

for u, v, val in G:
    if find_set(u) != find_set(v):

        Union(u, v)
        cost += val
        cnt += 1
    if cnt == N-2:
        break

print(cost)


    