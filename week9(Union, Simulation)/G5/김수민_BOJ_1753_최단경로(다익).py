# BOJ 1753 최단경로 - 디익스트라 골드 5 김수민
import heapq
V, E = map(int, input().split())
s = int(input()) - 1
INF = 1e9
cost = [[] for _ in range(V)]
D = [INF] * V # 시작점에서 각 인덱스까지의 최단경로
# 비용 담기
for _ in range(E):
    v, u, w = map(int, input().split())
    cost[v - 1].append((u - 1, w))
# 우선순위 큐로 연결된 애들 중 가중치 작은(비용 작은)비용으로 D 업데이트
H = []
heapq.heappush(H, (0, s))
D[s] = 0
while H:
    # 다음 탐색 노드 - 가장 최단 경로 짧은 노드
    dis, start = heapq.heappop(H)
    # 이미 검토 완료한 노드면 통과
    if D[start] < dis: continue
    # 연결된 애들 중에
    for node in cost[start]:
        # 도착노드의 저장된 최단경로 비용보다 현재 지점에서 비용 + 다음지점으로 가는 비용이 적으면
        # 즉 현재 노드를 거쳐가는 경우가 더 비용이 적게 들면
        if dis + node[1] < D[node[0]]:
            # D 값 업데이트
            D[node[0]] = dis + node[1]
            heapq.heappush(H, (D[node[0]], node[0]))
# 출력
for i in range(V):
    if D[i] == INF:
        print("INF")
    else: print(D[i])

