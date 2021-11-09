input = open('input.txt').readline



def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union(u, v):
    root_u, root_v = find_set(u), find_set(v)
    p[root_u] = root_v

while True:
    G = []
    total_cost = 0
    m, n = map(int, input().split())
    if m == 0 and n == 0: break

    for _ in range(n):
        u, v, val = map(int, input().split())
        total_cost += val

        G.append((u, v, val))

    G.sort(key=lambda x : x[2], reverse=True)

    p = [i for i in range(m+1)]

    mst = []

    min_cost = 0
    while len(mst) < m-1:

        u, v, val = G.pop()

        if find_set(u) != find_set(v):
            Union(u, v)
            min_cost += val
            mst.append((u, v))
    print(total_cost-min_cost)






