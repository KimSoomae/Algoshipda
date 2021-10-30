# 1197 최소 스패닝 트리 - 골드5 김수
import heapq
import collections
V, E = map(int, input().split())
# 빈그래프 생성 - 리스트를 초기값으로 가지는 딕셔너리
graph = collections.defaultdict(list)
# MSt 포함 여부
visited = [0] * (V + 1)
for _ in range(E):
    a, b, m = map(int, input().split())
    graph[a].append([m, a, b])
    graph[b].append([m, b, a])

def prim(graph, start):
    visited[start] = 1
    # 시작 노드에 연결된 애들이 후보
    candidate = graph[start]
    heapq.heapify(candidate) # 최소힙 - 가중치 기준
    MST = []
    total = 0
    while candidate:
        m, u, v = heapq.heappop(candidate)
        if visited[v] == 0:
            visited[v] = 1
            MST.append((u, v))
            total += m
            # 다음 정점에 연결된 애들
            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)
    return total

print(prim(graph, 1))