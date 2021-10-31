import heapq

n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [987654321] * (n+1) # 최단 거리 테이블을 큰 값으로 초기화

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 넣기
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 continue
        if distance[now] < dist:
            continue
        # for문 돌면서 현재 노드와 연결된 다른 노드들 체크
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == 987654321:
        print("INF")
    else:
        print(distance[i])