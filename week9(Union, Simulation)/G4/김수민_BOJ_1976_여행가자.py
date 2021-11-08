# BOJ 1976 여행가자 - 유니온 파인드: 골드 4 김수민
N = int(input())
M = int(input())

# x가 속한 집합 찾기. 즉 연결되어있는 여행 경로인지
def find_set(x):
    while x != P[x]:
        x = P[x]
    return x
# 두 도시가 연결되어있으면 같은 집합으로 합치기
def union(x, y):
    root_x, root_y = find_set(x), find_set(y)
    P[max(root_x, root_y)] = min(root_x, root_y)

P = [0] * (N + 1)
for i in range(N + 1):
    P[i] = i
cities = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 두 도시가 연결되어 있으면 union
        if cities[i][j] == 1:
            union(i + 1, j + 1)
travel = list(map(int, input().split()))
flag = True
for i in range(len(travel) - 1):
    # 여행 경로가 가능하지 않으면
    if find_set(travel[i]) != find_set(travel[i + 1]):
        flag = False
        break
if flag: print("YES")
else: print("NO")




