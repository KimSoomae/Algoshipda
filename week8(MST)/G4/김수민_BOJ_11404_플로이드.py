# 11404 플로이드 - 골드4 김수민
N = int(input())
M = int(input())
cost = [[1e9] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end, dis = map(int, input().split())
    cost[start][end] = min(dis, cost[start][end])

# 플로이드-와샬 알고리즘
for k in range(1, N + 1):
    cost[k][k] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cost[i][j] == 1e9:
            cost[i][j] = 0
        print(cost[i][j], end=' ')
    print()
