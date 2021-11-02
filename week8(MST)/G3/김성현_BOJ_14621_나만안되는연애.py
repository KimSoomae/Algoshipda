input = open('input.txt').readline

def Union(x, y):
    root_x, root_y = Find_set(x), Find_set(y)

    p[max(root_x, root_y)] = min(root_x, root_y)

def Find_set(x):
    while x != p[x]:
        x = p[x]
    return x

N, M = map(int, input().strip().split())
gender = [0] + list(input().strip().split())

G = []
for _ in range(M):
    u, v, d = map(int, input().strip().split())
    if gender[u] != gender[v]:
        G.append((u, v, d))

G.sort(key=lambda x : x[2])

p = [i for i in range(N+1)]
cnt = 0
result = 0

for u, v, d in G:
    if Find_set(u) != Find_set(v):
        Union(u, v)
        result += d
        cnt += 1

    if cnt == N-1:
        break


if cnt != N-1:
    result = -1

print(result)

