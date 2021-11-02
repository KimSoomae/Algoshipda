import math
import heapq
# 우주신들간 조합 만들고 거리 계산해서 간선을 나타내는 graph 리스트에 추가
def comb(cnt, start):
    if cnt == 2:
        a = path[0]; b = path[1]
        # 이미 연결된 우주신들은 거리 0으로
        if g[a][b] == 1:
            d = 0
        else:
            d = math.sqrt(math.pow(space[a][0] - space[b][0], 2) + math.pow(space[a][1] - space[b][1],2))
        graph.append((d, a, b))
        return
    for i in range(start, N + 1):
        visit[i] = 1
        path[cnt] = i
        comb(cnt + 1, i + 1)
        visit[i] = 0

# find 연산을 통해 사이클 확인
def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

# 두 집합을 하나로 합치는 연산
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

N, M = map(int, input().split())
space = [0] # 좌표 담을 리스트
graph = [] # (가중치, 노드1, 노드2)담을 리스트
p = [0] # 상호배타적 집합
for _ in range(N):
    x, y = map(int,input().split())
    space.append((x, y))

g = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # g[a][b]==1이면 a과 b가 이미 연결되어있음을 의미
    g[a][b] = 1
    g[b][a] = 1
# 처음엔 각 정점 자신이 집합의 대표인걸로 세팅
for i in range(1, N+1):
    p.append(i)

tree_edges = 0; tot = 0
path = [0] * 1002
visit = [0] * 1002
comb(0, 1) # 조합 찾기
heapq.heapify(graph) # 거리 기준 최소 힙
while True:
    # 간선 다 찾았으면 break
    if tree_edges == N - 1:
        break
    w, u, v = heapq.heappop(graph)
    # 사이클이 아니면 간선 선택되는 것
    if find(u) != find(v):
        union(u, v) # 노드 하나가 다른 노드의 대표로 설정하고
        tot += w # 정답에 거리(통로의 길이) 더해줌
        tree_edges += 1 # 간선의 개수 +1

print(f'{round(tot, 2):.2f}')


