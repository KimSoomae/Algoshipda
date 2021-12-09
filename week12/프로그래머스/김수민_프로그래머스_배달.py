# 프로그래머스 Summer/Winter Coding(~2018) 배달 - 2단계
import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    dis = [int(1e9)] * (N + 1)
    for i in range(len(road)):
        a, b, w = road[i]
        graph[a].append((b, w))
        graph[b].append((a, w))
    Q = []
    heapq.heappush(Q, (0, 1))
    dis[1] = 0
    while Q:
        dist, now = heapq.heappop(Q)
        if dis[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < dis[node[0]]:
                dis[node[0]] = cost
                heapq.heappush(Q, (cost, node[0]))
    for i in range(1, N + 1):
        if dis[i] <= K:
            answer += 1

    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)