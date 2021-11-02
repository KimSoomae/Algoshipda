# 11780 플로이드 2 - 골드3 김수민
N = int(input())
M = int(input())
# cost: 비용 계산 - 큰값으로 초기화, way: 최단 경로 담을 리스트
cost = [[1e9] * (N + 1) for _ in range(N + 1)]
way = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    start, end, dis = map(int, input().split())
    # 출발 - 도착 비용 담는데, 중복되는 버스 노선 있을 수 있으므로 최소값으로 갱신
    cost[start][end] = min(dis, cost[start][end])
    # 출발 도착 지점 경로로 지정
    if len(way[start][end]) == 0:
        way[start][end].append(start)
        way[start][end].append(end)
# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N + 1):
    cost[i][i] = 0

# 플로이드-와샬
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # k 거쳐가는 경우 경로 업데이트
            if (cost[i][k] + cost[k][j]) < cost[i][j]:
                way[i][j] = list()
                # i ~ k 까지의 경로
                for p in range(len(way[i][k])):
                    way[i][j].append(way[i][k][p])
                way[i][j].pop() # 중간에 k 겹치니까 pop
                # k ~ j 까지의 경로
                for p in range(len(way[k][j])):
                    way[i][j].append(way[k][j][p])
            # 저장된 최소비용과 k 거쳐가는 비용중 적은 비용으로 업데이트
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 최소비용 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cost[i][j] == 1e9:
            cost[i][j] = 0
        print(cost[i][j], end=' ')
    print()
# 경로 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # cnt: 최소 비용에 포함되어 있느 도시 개수
        cnt = len(way[i][j])
        if cnt == 0:
            print(0)
        else:
            print(cnt, end=' ')
            for k in range(cnt):
                print(way[i][j][k], end=' ')
            print()