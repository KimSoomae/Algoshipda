from itertools import combinations
input = open('input.txt').readline

def KRUSKAL(G):
    mst = []

    mst_cost = 0

    while len(mst) < N-1:
        u, v, val = G.pop()
        if Find_set(u) != Find_set(v):
            Union(u, v)
            mst_cost += val
            mst.append((u, v))

    return mst_cost


def Find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union(x, y):   
    root_x, root_y = Find_set(x), Find_set(y) 
    p[root_x] = root_y
    
N = int(input())
E = N * (N-1) // 2
stars = []

for i in range(N):
    x, y = map(float, input().split())
    stars.append((x, y, i+1))


lines = list(combinations(stars, 2))

G = []
while lines:
    two_stars = lines.pop()
    distance = round(((two_stars[0][0]-two_stars[1][0])**2 + (two_stars[0][1]-two_stars[1][1])**2)**0.5, 2)
    new_info = (two_stars[0][2], two_stars[1][2], distance)
    G.append(new_info)

G.sort(key=lambda x : x[2], reverse=True)
p = [i for i in range(N+1)]

result = '{:.2f}'.format(KRUSKAL(G))
print(result)

