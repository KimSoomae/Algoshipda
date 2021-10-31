# 크루스칼 알고리즘 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

v, e = map(int, input().split())
parent = [0] * (v + 1)
edges = []
ans = 0

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))  # 비용순으로 정렬하기 위해서
edges.sort()

for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않은 경우
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        ans += c

print(ans)