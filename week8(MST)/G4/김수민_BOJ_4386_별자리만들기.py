# 4386 별자리 만들기 - 골드4 김수민
from collections import defaultdict
import math
import heapq
# 가중치와 인접정점 담을 그래프
graph = defaultdict(list)
# 별자리 좌표간 조합 만들어서 거리, 정점들 그래프에 추가
def comb(cnt, start):
    if cnt == 2:
        a = path[0]; b = path[1]
        # 별들 간 거리 계산
        d = math.sqrt(math.pow(star[a][0] - star[b][0], 2) + math.pow(star[a][1] - star[b][1],2))
        graph[a].append([d, a, b])
        graph[b].append([d, b, a])
        return
    for i in range(start, N):
        visit[i] = 1
        path[cnt] = i
        comb(cnt + 1, i + 1)
        visit[i] = 0

N = int(input())
star = []
for _ in range(N):
    x, y = map(float, input().split())
    star.append((x, y))
path = [0] * 100
visit = [0] * 100
comb(0, 0)
# 프림 알고리즘 - 정점 골라서 연결된 애들 중에 가중치 짧은거 부터 MST에 포함시키기
visitstar = [0] * (N + 1) # MST에 포함여부
visitstar[0] = 1
candidate = graph[0]
heapq.heapify(candidate)
tot = 0
while candidate:
    # 최소힙이므로, 거리 짧은 애들부터 pop됨
    w, u, v = heapq.heappop(candidate)
    # 아직 MST에 포함되지 않은 애들이면 추가
    if visitstar[v] == 0:
        # MST에 추가
        visitstar[v] = 1
        tot += w
        # 연결된 애들 추가
        for edge in graph[v]:
            if visitstar[edge[2]] == 0:
                heapq.heappush(candidate, edge)
print(f'{tot:.2f}')